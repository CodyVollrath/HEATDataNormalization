import requests
import json
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
        self.tenant = tenant
        self.role = role
        PARAMS = {'tenant':tenant, 'username':username,'password':password, 'role':role}
        self.postReq = requests.post(url=postURL, data = PARAMS)

    def getBusinessObjectsByFilter(self, url, filter):
        queryKeyWord = "?$filter="
        url = url + queryKeyWord + filter
        return requests.get(url = url, params={"Authorization":self.getSessionID()}).json()

    def getBusinessObjectsByURLFilter(self, url):
        try:        
            key = url[url.index("?")+1:url.index("=")]
            value = url[url.index("=")+1:]
            url = url[:url.index("?")]
            param = {key : value}
        except: 
            print("BAD URL")
            return None
        headers = {"Authorization":self.getSessionID()}
        return requests.get(url = url, params = param, headers = headers).json()

    def getSessionID(self):
        return self.postReq.text.replace("\"","")

    def prettifyJson(self, jsonData):
        return json.dumps(jsonData, indent=2)

    def writeToFile(self, filename, data):
        try: 
            file = open(filename,"w+")
            file.write(data)
            return True
        except:
            return False
    
    def parseJson(self, jsonData):
        ticketDictionary = json.loads(jsonData)
        count = 0
        for item in ticketDictionary['value']:
            subject = item['Subject']
            createdDateTime = item['CreatedDateTime']
password = input("Enter pass: ")
test = heat_requests("https://southwire-stg.saasit.com/api/rest/authentication/login", "southwire-stg.saasit.com", "Vollrathco", password, "SelfService")

test.parseJson(test.prettifyJson(test.getBusinessObjectsByURLFilter("https://southwire-stg.saasit.com/api/odata/businessobject/incidents?$filter=Status eq 'Active'")))