from model.heat_requests import heat_requests

if __name__ == "__main__":
    heat = heat_requests("https://southwire-stg.saasit.com/api/rest/authentication/login", "southwire-stg.saasit.com", "Vollrathco", "Xxvc79x11#", "SelfService")
    print(heat.getBusinessObjectsByURLFilter("https://southwire-stg.saasit.com/api/odata/businessobject/incidents?$filter=Status eq 'Active'"))
    if (heat.getTickets().writeTicketToFile("../files/tickets.txt")):
        print("Tickets written to file")
    heat.getTickets().generateReports("../files/ticketTest.xlsx")