# Jackson Hauley, Gavin Pierce, Lizzy Saldana, Luke Murdock

import random
import time

# Initializing Variables
artist_list = []
tickets = []
id = 0


# Defining Funcitons

def main():
    while True:
        cs()
        choice = int_input("MUSIC FESTIVAL\n\n1. Information\n2. Tickets\n3. Schedule\n4. Artists\n5. Recommendation\n6. Exit\n\nChoose one (1-6): ")
        if choice == 1: # Information
            pass
        elif choice == 2: # Tickets
            ticket_main()
        elif choice == 3: # Schedule
            pass
        elif choice == 4: # Artist List
            artist_main()
        elif choice == 5: # Recommendation
            pass
        elif choice == 6: # Exit
            cs()
            print('Thanks for attending!')
            exit()

def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError:
            print("Invalid Input! (only integers accepted)") # Invalid Input Text
            input("Press enter to try again")
            continue
        return output
    
def str_input(text): # Only takes in string
    while True:
        try: output = str(input(text))
        except ValueError:
            print("String Input! (only strings accepted)") # Invalid Input Text
            input("Press enter to try again")
            continue
        return output
    
def float_input(text): # Only takes in floats
    while True:
        try: output = float(input(text))
        except ValueError:
            print("Invalid Input! (only floats accepted)") # Invalid Input Text
            input("Press enter to try again")
            continue
        return output

def ticket_main(): # Ticket main function (runs all ticket information through here) ((jacksons function))
    while True:
        cs()
        choice = int_input("TICKET MENU\n\n1. Buy Ticket\n2. Search Tickets\n3. Ticket Informatoin\n4. Ticket Sales Report\n5. Exit\n\nChoose one (1-5): ")
        if choice == 1: # Buy Ticket
            buy_ticket()
        elif choice == 2: # Search Tickets
            pass
        elif choice == 3: # Ticket Informatoin
            pass
        elif choice == 4: # Ticket Sales Report
            pass
        elif choice == 5: # Exit
            main()

def buy_ticket(): # Buy a ticket (Jacksons Function)
    global id
    ticket = []
    cs()
    print("Buying Ticket\n") # Visual
    firstname = input("What is your first name?: ") # Name Input
    lastname = input("What is your last name?: ")
    age = int_input("How old are you?: ") # Age Selection
    if 120 < age or age < 0:
        randage = random.randint(1,10)
        print(f"Bro there is no way your that age, I bet your {randage}") # Dissing on people who are joking around
        age = randage
    while True:
        membership_choice = int_input("\nWhat membership level do you want to buy?\n1. NPC\n2. VIP\n3. MVP\n\nType number here (1-3): ") # Membership Level Selection
        if membership_choice == 1:
            membership = 'NPC' # NPC membership setting
            cost = 19.99
            break
        elif membership_choice == 2:
            membership = 'VIP' # VIP membership setting
            cost = 49.99
            break
        elif membership_choice == 3:
            membership = 'MVP' # MVP membership setting
            cost = 99.99
            break
        else:
            print("Invalid Input (1-3)")
            input("Press enter to continue")
    while True:
        duration_choice = int_input("\nHow long do you want this ticket to work?\n1. 1 day\n2. 3 days\n3. 1 week\n4. 1 month\n5. season pass\n\nType number here (1-5): ") # Duration Selection
        if duration_choice == 1: # These are for how long your ticket works
            duration = "1 day" # 1 day duration
            cost += 0
            break
        elif duration_choice == 2:
            duration = "3 days" # 3 days duration
            cost += 40
            break
        elif duration_choice == 3:
            duration = "1 week" # 1 week duration
            cost += 80
            break
        elif duration_choice == 4:
            duration = "1 month"  # 1 month duration
            cost += 120
            break
        elif duration_choice == 5:
            duration = "season pass" # season pass
            cost += 300
            break
        else:
            print("Invalid Input (1-3)") # Error Handling
            input("Press enter to continue")

    print(f"\nMembership {membership} selected") # Visual
    print(f"This ticket will last {duration}!")
    print(f"Cost: ${cost}")
    quick_choice1 = str_input("\nType yes to confirm, anything else will cancel: ") # Confirming Information
    if quick_choice1 == "yes":
        cs()
        print(f"Buying {membership} ticket") # Buying Ticket
        creditcard = int_input("Enter credit card number, with no spaces (1234123412341234): ") # Getting money
        cvv = int_input("Enter CVV number, with no spaces (123): ")
        quick_choice2 = str_input("\nType yes to confirm, anything else will cancel: ") # Confirming Information
        if quick_choice2 == "yes":
            print("\nTicket Bought!\n")
            id += 1
            print(f"Ticket ID: {id}")
            print(f"""
████████████████████████████████████████████████
█   WMWMW   | Name: {firstname:<15} {lastname:<15} █
█  /     \\  | Age: {age:<5}                      █
█  |O   O|  | Membership Level: {membership:<5}   █
█  |  L  |  | Date Bought: {time.ctime():<20}      █
█   \ W /   | Duration: {duration:<15}             █
█    | |    | ID: {id:<10}                         █
████████████████████████████████████████████████""") # Printing out their ticket
            input("Press enter to continue")
        else:
            print("Ticket Canceled!")
            input("Press enter to continue")
    else:
        print("Ticket Canceled!")
        input("Press enter to continue")
    



        


def cs(): # Clear Screen
    print("\033c",end="")

# Luke's Functions
def artist_main(): # 
    while True:
        cs()
        choice = int_input("Artist List\n\n1. Display\n2. Add\n3. Remove\n4. Edit\n5. Exit")
        if choice == 1:
            print(f"Artist List: {artist_list}")
        elif choice == 2:
            add_artist()
        elif choice == 3:
            remove_artist()
        elif choice == 4:
            edit_artist(int_input("What do you want changed?\nName(1) Genre(2) Time(3)"))
        else:
            break

def add_artist(): #
    print("Adding An Artist")
    artist_name = str_input("What is the artist's name?")
    artist_genre = str_input("What is the artist's genre?")
    artist_time = str_input("What is the artist's time dutation?")

def remove_artist(): #
    pass
def edit_artist(change_type): #
    pass

# Running Code

main()