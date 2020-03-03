from model.heat_requests import heat_requests
import asyncio
def generateIncidents(dateToStop):
    print("Logging in")
    heat = heat_requests("https://southwire.saasit.com/api/rest/authentication/login", "southwire.saasit.com", "Vollrathco", "Xxvc79x11#", "SelfService")
    print("loading tickets from HEAT")
    print(heat.getBusinessObjectsByURLFilter("https://southwire.saasit.com/api/odata/businessobject/incidents?$orderby=CreatedDateTime desc", "02/01/2020 | 12:00:00AM"))
    print("Tickets received - Writing data to ticketText...")
    heat.getTickets().generateReports("../files/ticketTest.xlsx")
    print("Finished")

def generateServiceReq(dateToStop):
    print("Logging in")
    heat = heat_requests("https://southwire.saasit.com/api/rest/authentication/login", "southwire.saasit.com", "Vollrathco", "Xxvc79x11#", "SelfService")
    print("loading tickets from HEAT")
    print(heat.getBusinessObjectsByURLFilter("https://southwire.saasit.com/api/odata/businessobject/ServiceReqs?$orderby=CreatedDateTime desc", dateToStop))
    print("Tickets received - Writing data to ticketText...")
    heat.getTickets().generateReports("../files/ticketTest2.xlsx")
    print("Finished")
def main():
    # await asyncio.gather(generateIncidents("03/03/2020 | 09:00:00AM"), generateServiceReq("03/03/2020 | 09:00:00AM"))
    generateIncidents("03/03/2020 | 09:00:00AM")
    generateServiceReq("03/03/2020 | 09:00:00AM")
if __name__ == "__main__":
    main()