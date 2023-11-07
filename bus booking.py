class Bussytem:
    def __init__(self):
        self.users={}
        self.buses=[]
        self.admin_password="admin@2023"


    def add_user(self,username,password):
        self.user[username]=password
    def admin_login(self,username,password):
        if password==self.admin_password:
            return True
        else:
            return False

    def user_login(self,username,password):
        if password==self.user[username]:
            return True
        else:
            return False

    #Admin functions
    #A)add
    def add_details(self,bus_name,seats,occupancy,num_of_days,source,destination):
        self.buses.append({
            "bus_name":bus_name,
            "seats":seats,
            "occupancy":occupancy,
            "days_of_operation":num_of_days,
            "source":source,
            "destination":destination
        })

    #B)update 
    def update_details(self,bus_name,seats,occupancy,num_of_days):
        for bus in self.buses:
            if bus["bus_name"]==bus_name:
                bus["seats"]=seats
                bus["occupancy"]=occupancy
                bus["days_of_operation"]=num_of_days

    #C)delete
    def delete_bus(self,bus_name,seats,occupancy,num_of_days):
        for bus in self.buses:
            if bus["bus name"]==bus_name:
                self.buses.remove(bus)

    #users function
    #A)book a seat

    def book_seat(self,username,password,bus_name,occupancy,seats,seats_req):
        for bus in self.buses:
            if bus["bus_name"]==bus_name:
                if bus["occupancy"]>=0.8*seats:
                    print("Sorry! There are no more tickets available in this bus. Kindly book a ticket in another bus")
                    
                else:
                    if bus["seats"]>=seats_req:
                        bus["seats"]-=seats_req
                        print("Ticket booked for"+seats_req+"passengers"+"in the bus"+bus_name)
                    else:
                        print("Sorry! There are no more tickets available in this bus. Kindly book a ticket in another bus")
                return
        print("Sorry bus not found")

    #B)cancel a seat
    def cancel_seat(self,username,password,bus_name,seats_req):
        for bus in self.buses:
            if bus["bus_name"]==bus_name:
                for booked_ticket in bus.get("booked_ticket",[]):
                    if booked_ticket["username"]==username and booked_ticket["password"]==password and booked_ticket["seats_req"]==seats_req:
                        bus["seats"]+=seats_req
                        bus["book_tickets"].remove(booked_ticket)
                        print("Your ticket has been cancelled")
                        return
                print("No matching booked ticket found")
                return
        print("No bus found")

    #C) checking number of seats
    def check_num_of_seats(self,bus_name):
        for bus in self.buses:
            if bus["bus_name"]==bus_name:
                ans= bus["seats"]
                print("There are"+ans+"seats available in this bus")
                return
        print("No such bus found")

    #D) checking number of buses between  source and destination
    def find_buses(self,source,destination):
        matching_buses=[]
        for bus in self.buses:
            if source in bus["source"] and destination in bus["destination"]:
                matching_buses.append(bus)
        
        print("Number of buses between "+source+" and "+destination+" are "+len(matching_buses))
        return matching_buses
        
bussys=Bussytem()    



