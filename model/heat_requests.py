import requests
import json
import FormaterData
from Ticket import Ticket
from Ticket_Library import Ticket_Library
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
    def __init__(self, postURL,tenant, username, password, role):
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
        self.postReq = requests.post(url=postURL, data = PARAMS)
        self.__tickets = Ticket_Library()
        self.__ticketNumber = 0

    def getBusinessObjectsByURLFilter(self, url):
        try:
            newURL = url[:url.index("?")]
            param = self.__configureParams(url)
            headers = {"Authorization":self.getSessionID()}
            jsonData = self.__prettifyJson(requests.get(url = newURL, params = param , headers = headers).json())
            self.parseJson(jsonData)
            self.getBusinessObjectsByURLFilter(url)
            return "Total Incidents: " + str(self.__tickets.length())
        except Exception as e:
            return e
        
    def __configureParams(self, url):
        filterKey = url[url.index("?")+1:url.index("=")]
        filterValue = url[url.index("=")+1:]
        return  {filterKey : filterValue, "$skip":str(self.__ticketNumber)}
    def getSessionID(self):
        return self.postReq.text.replace("\"","")

    def __prettifyJson(self, jsonData):
        return json.dumps(jsonData, indent=2)

    def getTickets(self):
        return self.__tickets

    def parseJson(self, jsonData):
        ticketData = json.loads(jsonData)
        for item in ticketData['value']:
            self.__ticketNumber += 1
            subject = item['Subject']
            owner = item['Owner']
            ownerTeam = item['OwnerTeam']
            ownerEmail = item['OwnerEmail']
            createdDateTime = FormaterData.formatDateTime(item['CreatedDateTime'])
            incidentNumber = item['IncidentNumber']
            status = item['Status']
            typeData = "Incident"
            ticket = Ticket(subject, owner, ownerTeam, ownerEmail,createdDateTime, incidentNumber, status,typeData)
            self.__tickets.add(ticket)