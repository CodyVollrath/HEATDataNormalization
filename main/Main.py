from model.heat_requests import heat_requests

if __name__ == "__main__":
    print("Logging in")
    heat = heat_requests("https://southwire.saasit.com/api/rest/authentication/login", "southwire.saasit.com", "Vollrathco", "Xxvc79x11#", "SelfService")
    print("loading tickets from HEAT")
    print(heat.getBusinessObjectsByURLFilter("https://southwire.saasit.com/api/odata/businessobject/incidents?$orderby=CreatedDateTime desc", "01/25/2020 | 12:00:00AM"))
    print("Incidents received - Writing data to ticketText...")
    heat.getTickets().generateReports("../files/ticketTest.xlsx")
    print("Finished")