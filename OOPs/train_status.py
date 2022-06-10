class Train:

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def status(self):
        print(f"Name of the Train is {self.name}")
        print(f"Total Number of seats remaining are {self.seats}")
    
    def getInfo(self):
        print(f"The Price of the Ticket is Rs. {self.fare}")

    def getTicket(self ):
        if (self.seats > 0):
            print(f"Your seat is booked successfully & Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, Seats are not available in this Train.")    

    
interacity = Train("Intracity", 90, 300) 
interacity.status()
interacity.getTicket()
interacity.getInfo()
interacity.status()