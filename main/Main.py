from model.heat_requests import heat_requests

if __name__ == "__main__":
    print("Logging in")
    heat = heat_requests("https://southwire-stg.saasit.com/api/rest/authentication/login", "southwire-stg.saasit.com", "Vollrathco", "Xxvc79x11#", "SelfService")
    print("loading tickets from HEAT")
    print(heat.getBusinessObjectsByURLFilter("https://southwire-stg.saasit.com/api/odata/businessobject/incidents?$filter=Status eq 'Active'"))
    print("Incidents received - Writing data to ticketText...")
    heat.getTickets().generateReports("../files/ticketTest.xlsx")
    print("Finished")