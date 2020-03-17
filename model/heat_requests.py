import requests
import json
import controller.FormaterData as FormaterData
import controller.fileHandler as fileHandler
from model.Incident import Incident
from model.Ticket_Library import Ticket_Library
from model.Service_Request import Service_Request
class heat_requests:
    """
    Description: The heat_requests API Wrapper
    Allows POST and GET requests via the Ivanti Heat Ticketing System REST API
    The wrapper will abstract the functions so that it feels more pythonic
    META
    -------------
    Author: Cody Vollrath
    Version: 1.0
    Owner: Southwire

    Attributes
    --------------
    private postURL: str
        The url that will be used to login
    tenant: str
        A string that represents the domain for the business set up with ivanti
    username: str
        The login username for the client using Ivanti to extract the data via the api
    password: str
        The login password for the client using Ivanti to extract the data via the api
    role: str
        The role of the user entering the data


    Methods
    --------------
    TBA
    """
    def __init__(self, postURL="",tenant="", username="", password="", role=""):
        """
        Constucts a heat_request object and instantiates potentially needed data members
        PARAMS
        --------------
        postURL : str 
            Serves as the temp url to post too. Although passed to the constructer it is not a data member, merely used to make a post request to the api url
        tenant : str
            The tenant is the doman of the company you are connecting too. This only includes the top level domain as well as any primary/secondary/tertiary domains.
        username : str 
            The username of the user
        password : str
            The password of the user
        role : str
            The role of the user
        """
        PARAMS = {'tenant':tenant, 'username':username,'password':password, 'role':role}
        if not postURL == "":
            self.postReq = requests.post(url=postURL, data = PARAMS)
        else:
            self.postReq = ""
        self.__tickets = Ticket_Library()
        self.__ticketNumber = 0

    def getBusinessObjectsByURLFilter(self, url, dateToStop):
        try:
            isIncident = "incidents" in url
            newURL = url[:url.index("?")]
            param = self.__configureParams(url)
            headers = {"Authorization" : self.getSessionID()}
            jsonData = json.dumps(requests.get(url = newURL, params = param , headers = headers).json())
            if self.getTicketData(isIncident, jsonData, dateToStop):
                self.getBusinessObjectsByURLFilter(url, dateToStop)
            print("Total Tickets: " + str(self.__tickets.length()))
            return True
        except Exception as e:
            print(fileHandler.writeErrorToLog(e))
            return False

    def __configureParams(self, url):
        filterKey = url[url.index("?")+1:url.index("=")]
        filterValue = url[url.index("=")+1:]
        return  {filterKey : filterValue, "$skip" : str(self.__ticketNumber), "$top" : 100}

    def getSessionID(self):
        return fileHandler.getSessionId()

    def __prettifyJson(self, jsonData):
        return json.dumps(jsonData, indent=2)

    def getTickets(self):
        return self.__tickets
    def getTicketData(self, isIncident, jsonData, dateToStop):
        if isIncident:
            return self.getIncidents(jsonData, dateToStop)
        else:
            return self.getServiceReqs(jsonData, dateToStop)
    def getIncidents(self, jsonData, dateToStop):
        ticketData = json.loads(jsonData)
        for item in ticketData['value']:
            if FormaterData.isDateLessThanOrEqualTo(dateToStop, FormaterData.formatDateTime(item['CreatedDateTime'])):
                subject = item['Subject']
                creator = item['CreatedBy']
                owner = item['Owner']
                ownerEmail = item['OwnerEmail']
                ownerTeam = item['OwnerTeam']
                service = item['Service']
                createdDateTime = FormaterData.formatDateTime(item['CreatedDateTime'])
                resolveDate = FormaterData.formatDateTime(item['ResolvedDateTime'])
                incidentNumber = item['IncidentNumber']
                print("Incident number: " + str(incidentNumber) + " is being fetched")
                status = item['Status']
                typeData = "Incident"
                firstCall = item["FirstCallResolution"]
                ticket = Incident(subject, creator, owner, ownerEmail, ownerTeam, service, createdDateTime, resolveDate,
                                  incidentNumber, status, typeData,firstCall)
                print("Ticket Added: " + str(self.__tickets.add(ticket)))
                self.__ticketNumber += 1
                print(self.__ticketNumber)
            else:
                return False
        return True

    def getServiceReqs(self, jsonData, dateToStop):
        ticketData = json.loads(jsonData)
        for item in ticketData['value']:
            if FormaterData.isDateLessThanOrEqualTo(dateToStop, FormaterData.formatDateTime(item['CreatedDateTime'])):
                subject = item['Subject']
                creator = item['CreatedBy']
                ownerEmail = item['OwnerEmail']
                typeData = "Service Request"
                service = item['Service']

                servReqId = item['ServiceReqNumber']
                print("Service Request: " + str(servReqId) + " is being fetched")
                status = item['Status']
                ownerTeam = item['OwnerTeam']
                owner = item['Owner']
                createdOn = FormaterData.formatDateTime(item['CreatedDateTime'])
                resolvedOn = FormaterData.formatDateTime(item['ResolvedDateTime'])
                ticket = Service_Request(subject, creator, owner, ownerEmail, ownerTeam, service, createdOn, resolvedOn, servReqId, status, typeData)
                print("Ticket Added: " + str(self.__tickets.add(ticket)))
                self.__ticketNumber += 1
                print(self.__ticketNumber)
            else:
                return False
        return True

