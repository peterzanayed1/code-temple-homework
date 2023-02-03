class parking_Garage():
    
    def __init__(self, current_ticket = {'paid' : False,} ,price = 5 ,spaces_available= 100):
        self.current_ticket = current_ticket
        self.price = price
        self.spaces_available = spaces_available
        self.hours = ''
    
    def take_Ticket(self):
        (self.spaces_available) -= 1
        print( f"{self.spaces_available} spaces are left")
    
    def pay_for_parking(self):
        hours_parked = input("Enter how many hours you were parked")
        total_owed = int(self.price * int(hours_parked))
        print(f"you owe ${total_owed}")
        payment_amount = input('how much are you paying?')
        if int(payment_amount) == total_owed:
            self.current_ticket['paid'] = True
            print('Ticket has been paid you have 15 minutes to exit the garage')
        else:
            print('This is not the correct amount to pay')

    def leave_Garage(self):
        if self.current_ticket['paid'] == True:
            self.spaces_available += 1
            print('Thank you, have a nice day')
        else:
            hours_parked = input("Enter how many hours you were parked")
            total_owed = int(self.price * int(hours_parked))
            print(f"you owe ${total_owed}")
            payment_amount = input('how much are you paying?')
            if int(payment_amount) == total_owed:
                self.current_ticket = True
                self.spaces_available += 1
                print('Ticket has been paid you have 15 minutes to exit the garage')
            else:
                print('This is not the correct amount to pay' "you have to pay before exiting the garage")



garage = parking_Garage()
garage.take_Ticket()
garage.take_Ticket()
garage.take_Ticket()
garage.take_Ticket()
garage.pay_for_parking()
garage.leave_Garage()
garage.take_Ticket()

        

        
