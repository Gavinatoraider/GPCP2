# Jackson Hauley, Gavin Pierce, Lizzy Saldana, Luke Murdock

import random

# Initializing Variables
tickets = []

# Defining Funcitons

def main():
    while True:
        cs()
        choice = int_input("MUSIC FESTIVAL\n\n1. Information\n2. Tickets\n3. Schedule\n4. Recommendation\n5. Exit")
        if choice == 1: # Information
            pass
        elif choice == 2: # Tickets
            pass
        elif choice == 3: # Schedule
            pass
        elif choice == 4: # Recommendation
            pass
        elif choice == 5: # Exit
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

def buy_ticket(): # Buy a ticket (Jacksons Function)
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
    print(f"Membership {membership} selected") # Visual
    print(f"Cost: ${cost}")
    input("\nType yes to confirm, anything else will cancel: ") # Confirming Information
    if input == "yes":
        cs()
        print(f"Buying {membership} ticket") # Buying Ticket
        creditcard = int_input("Enter credit card number, with no spaces (1234123412341234): ")
        ccv = int_input("Enter CVV number, with no spaces (123): ")
        input("\nType yes to confirm, anything else will cancel: ") # Confirming Information
        if input == "yes":
            print("\nTicket Bought!\n")
            print(f"""
-------------------------------------------------------------------
|  ///-\\\\ | Name: {firstname} {lastname}
|  |^   ^|  | Age: {age}
|  |O   O|  |
|  |  ~  |  |
|   \ U /   |
|    | |    |
-------------------------------------------------------------------""")
    



        


def cs(): # Clear Screen
    print("\033c",end="")

# Running Code

main()