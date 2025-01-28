# Jackson Hauley, Gavin Pierce, Lizzy Saldana, Luke Murdock

artist_scheduale= []

password = ("MusicFestival1234")
password_attepmt = 3

loop_num=0

num_of_preformences=(15)

import random
import time

# Initializing Variables
artist_list = []
tickets = []
id = 0
female_ratio = 0
male_ratio = 0
tickets_bought = 0
total_money = 0
memberships_bought = []
durations_bought = []
age_list = []


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

def cs(): # Clear Screen
    print("\033c",end="")



def ticket_main(): # Ticket main function (runs all ticket information through here) ((jacksons function))
    while True:
        cs()
        choice = int_input("TICKET MENU\n\n1. Buy Ticket\n2. Search Tickets\n3. Ticket Information\n4. Ticket Sales Report\n5. Generate Random People\n6. Exit\n\nChoose one (1-6): ")
        if choice == 1: # Buy Ticket
            buy_ticket()
        elif choice == 2: # Search Tickets
            search_tickets()
        elif choice == 3: # Ticket Informatoin
            ticket_information()
        elif choice == 4: # Ticket Sales Report
            ticket_report()
        elif choice == 5: # Random People Generator
            gen_rand_ticket(total_money,tickets_bought,male_ratio,female_ratio,id)
        elif choice == 6: # Exit
            pass
        elif choice == 5: # Exit
            main()

def gen_rand_ticket(total_money,tickets_bought,male_ratio,female_ratio,id): # Random Ticket Generator
    cs()
    amount = int_input("How many tickets do you want to generate?: ")
    print()
    for x in range(amount):
        firstname = random.choice(["Jackson","Gavin","Nicole","Luke","Lizzy","Hauley","Saldana","Murdock","Pierce"])
        lastname = random.choice(["Jackson","Gavin","Nicole","Luke","Lizzy","Hauley","Saldana","Murdock","Pierce"])
        age = random.choice(list(range(1,120)))
        membership = random.choice(["NPC","VIP","MVP"])
        duration = random.choice(["1 Day","3 Day","1 Week","1 Month","Season Pass"])
        cost = random.randint(100,400)
        id += 1
        creditcard = random.randint(1000000000000000,9999999999999999)
        cvv = random.randint(100,999)
        ticket_time = time.ctime()
        gender = random.choice(["Male","Female"])
        ticketlist = [firstname,lastname,age,membership,duration,cost,id,creditcard,cvv,ticket_time,gender]
        tickets.append(ticketlist) # First, Last, Age, Member, Duration, Cost, ID, CC, CVV, TIME, gender
        print(f"Ticket Created! [ID: {id}]")
    input("\nFINISHED GENERATING\nPress enter to continue")

def search_tickets(): # Search tickets 
    cs()
    print("Search All Tickets")
    search_keyword = input("Enter any keyword or ID to try and find a ticket: ") # First, Last, Age, Member, Duration, Cost, ID, CC, CVV, TIME,gender
    print()
    for x in range(len(tickets)):
        for i in tickets[x]:
            if i == search_keyword:
                print(f"Name: {tickets[x][0]} {tickets[x][1]}   ID: {tickets[x][6]}")
    search_ID = int_input("\nWhich ticket do you want to open? (ID): ")
    print()
    for x in range(len(tickets)):
        if tickets[x][6] == search_ID:
            if tickets[x][10] == "Male":
                print(f"""
    ██████████████████████████████████████████████████████
    █   WMWMW   █ Name: {tickets[x][0]} {tickets[x][1]}
    █  /     \\  █ Age: {tickets[x][2]} Gender: {tickets[x][10]}                 
    █  |O   O|  █ Membership Level: {tickets[x][3]}   
    █  |  L  |  █ Date Bought: {tickets[x][9]}  
    █   \ U /   █ Duration: {tickets[x][4]}         
    █    | |    █ ID: {tickets[x][6]}                     
    ██████████████████████████████████████████████████████""") # Printing out their ticket
            else:
                print(f"""
    ██████████████████████████████████████████████████████
    █   WMWMW   █ Name: {tickets[x][0]} {tickets[x][1]}
    █  W     W  █ Age: {tickets[x][2]} Gender: {tickets[x][10]}                 
    █ W|O   O|W █ Membership Level: {tickets[x][3]}   
    █ M|  L  |M █ Date Bought: {tickets[x][9]}  
    █   \ U /   █ Duration: {tickets[x][4]}         
    █    | |    █ ID: {tickets[x][6]}                     
    ██████████████████████████████████████████████████████""") # Printing out their ticket
            print(f"\nCost: ${tickets[x][5]}")
            print(f"Credit Card: {tickets[x][7]}")
            print(f"CVV: {tickets[x][8]}")
            input("Press enter to continue")
            break


def ticket_report(): # Ticket report 
    pass

def buy_ticket(): # Buy a ticket (Jacksons Function)
    global id
    ticket = []
    cs()
    print("Buying Ticket\n") # Visual
    firstname = input("What is your first name?: ") # Name Input
    lastname = input("What is your last name?: ")
    age = int_input("How old are you?: ") # Age Selection
    if 120 < age or age < 0:
        randage = random.randint(1,random.randint(10,random.randint(11,18)))
        print(f"\nBro there is no way your that age, I bet your {randage}") # Dissing on people who are joking around
        age = randage
    while True:
        gender_choice = input("Male or Female? (m/f): ") # chooses gender
        if gender_choice.lower()  == "m":
            gender = "Male"
            break
        elif gender_choice.lower() == "f":
            gender = "Female"
            break
        else:
            print("Invalid Input (m/f)")
            input("Press enter to continue")
    while True:
        membership_choice = int_input("\nWhat membership level do you want to buy?\n1. NPC ($19.99)\n2. VIP ($49.99)\n3. MVP ($99.99)\n\nType number here (1-3): ") # Membership Level Selection
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
        duration_choice = int_input("\nHow long do you want this ticket to work?\n1. 1 day (+$0.00)\n2. 3 days (+$40.00)\n3. 1 week (+$80.00)\n4. 1 month (+$120.00)\n5. Season pass (+$300.00)\n\nType number here (1-5): ") # Duration Selection
        if duration_choice == 1: # These are for how long your ticket works
            duration = "1 Day" # 1 day duration
            cost += 0
            break
        elif duration_choice == 2:
            duration = "3 Days" # 3 days duration
            cost += 40
            break
        elif duration_choice == 3:
            duration = "1 Week" # 1 week duration
            cost += 80
            break
        elif duration_choice == 4:
            duration = "1 Month"  # 1 month duration
            cost += 120
            break
        elif duration_choice == 5:
            duration = "Season Pass" # season pass
            cost += 300
            break
        else:
            print("Invalid Input (1-3)") # Error Handling
            input("Press enter to continue")

    print(f"\nMembership {membership} selected") # Visual
    print(f"This ticket will last {duration}!")
    print(f"Cost: ${cost}")
    quick_choice1 = input("\nType yes to confirm, anything else will cancel: ") # Confirming Information
    if quick_choice1 == "yes":
        cs()
        print(f"Buying {membership} ticket") # Buying Ticket
        creditcard = int_input("Enter credit card number, with no spaces (1234123412341234): ") # Getting money
        cvv = int_input("Enter CVV number, with no spaces (123): ")
        quick_choice2 = input("\nType yes to confirm, anything else will cancel: ") # Confirming Information
        if quick_choice2 == "yes":
            print("\nTicket Bought!\n")
            id += 1
            print(f"Ticket ID: {id}")
            ticket_time = time.ctime()
            if gender == "Male":
                print(f"""
    ██████████████████████████████████████████████████████
    █   WMWMW   █ Name: {firstname} {lastname}
    █  /     \\  █ Age: {age} Gender: {gender}             
    █  |O   O|  █ Membership Level: {membership}   
    █  |  L  |  █ Date Bought: {ticket_time}  
    █   \ W /   █ Duration: {duration}         
    █    | |    █ ID: {id}                     
    ██████████████████████████████████████████████████████""") # Printing out their ticket
            else:
                print(f"""
    ██████████████████████████████████████████████████████
    █   WMWMW   █ Name: {firstname} {lastname}
    █  W     W  █ Age: {age} Gender: {gender}                 
    █ W|O   O|W █ Membership Level: {membership}  
    █ M|  L  |M █ Date Bought: {ticket_time}  
    █   \ U /   █ Duration: {duration}         
    █    | |    █ ID: {id}                     
    ██████████████████████████████████████████████████████""") # Printing out their ticket
            input("\nPress enter to continue")
        else:
            print("Ticket Canceled!")
            input("Press enter to continue")
    else:
        print("Ticket Canceled!")
        input("Press enter to continue")
    ticketlist = [firstname,lastname,age,membership,duration,cost,id,creditcard,cvv,ticket_time,gender]
    tickets.append(ticketlist) # First, Last, Age, Member, Duration, Cost, ID, CC, CVV, TIME, gender
    
def ticket_information(): # Prints out ticket information (anyone change this if you want and its a good idea no stupid stuff)
    cs()
    print(f"""
TICKET INFORMATION

Membership Levels:
    NPC ($19.99)
The most basic pass, provides you with all concerts/artist shows in public seating
    VIP ($49.99)
The 2nd best pass, gives you a special fast lane in all lines and VIP seating zone, plus you get to meet an artist
    MVP ($99.99)
THE BEST pass you can buy, gives extremely fast lines and 50% off everything in the convention, meet all artists/performers and free merch + candy + 1 meal/day
          
Duration Levels:
    1 Day: 1 day in the convention from 7:00am to 10:00pm
    3 Day: 3 days in the convention from 7:00am to 10:00pm (2 overnights)
    1 Week: 7 days in the convention from 7:00am to 10:00pm (6 overnights)
    1 Month: 30 days in the convention from 7:00am to 10:00pm (29 overnights)
    Season Pass: Full season access to the convention any time, 1 free meal a day (stackable with MVP)

Your information is kept in a secure online server with {random.randint(1,1000)} firewalls protecting it RIGHT NOW
          """)   
    input('Press enter to continue')


        




# Luke's Functions
def artist_main(): # 
    while True:
        cs()
        choice = int_input("\nArtist List Management\n\n1. Display\n2. Add\n3. Remove\n4. Edit\n5. Exit\n")
        if choice == 1:
            print(f"Artist List: {artist_list}")
            input()
        elif choice == 2:
            add_artist()
        elif choice == 3:
            remove_artist()
        elif choice == 4:
            edit_artist(int_input("What do you want changed?\nName(1) Genre(2) Time(3)\n"))
        else:
            break

def add_artist(): #
    print("Adding An Artist")
    artist_name = str_input("What is the artist's name?:\n")
    artist_genre = str_input("What is the artist's genre?:\n")
    artist_time = str_input("What is the artist's time duration in minutes?:\n")

    artist_list.append([artist_name, artist_genre, artist_time])

def remove_artist(): #
    removed = 0
    print("Removing An Artist")
    artist_name = str_input("What is the artist's name?:\n")

    for artist in artist_list:
        if artist_name.title() == artist[0].title():
            artist_list.remove(artist)
            removed = 1
    if removed == 0:
        print("Not in List\nClick Enter to Continue")
        input()

def edit_artist(change_type): #
    print("Editing An Artist")
    artist_name = str_input("What is the artist's name?:\n")
    while True:
        change_type = int_input("What do you want changed?\nName(1) Genre(2) Time(3)\n") -1
        if change_type < 0 or change_type > 2:
            print("Not in Range (1-3)")
            continue
        break
    new_text = str_input("What do you want it changed to?:\n")

    for artist_num, artist in enumerate(artist_list):
        if artist_name.title() == artist[0].title():
            artist_list[artist_num][change_type] = new_text
            edited = 1
    if edited == 0:
        print("Not in List\nClick Enter to Continue")
        input()

def search_artist():
    artist_results = []
    print("Searching For An Artist")
    artist_search = str_input("Search for the artist through their name, genre, or time:\n").upper()
    for artist in artist_list:
        for fact in artist:
            if artist_search in fact.upper():
                artist_results.append(artist)
                break
    print(f"Results: {artist_results}\nClick Enter to Continue")
    input()




# Gavins code
    for artist in artist_list:
        if artist_name == artist[0]:
            artist_list[change_type] = new_text

# Running Code

#Gavins code

# the schedule
#the schedaul


# adds people to schedule
def schedule_add():
    artist_add=input("what is the artist's name?")
    artist_scheduale.append(artist_add)
    loop_num+=1
    print(artist_list)

# removes from schedule
def schedule_remove():
    while password_attepmt <=0:
        verifide=input("what is the password?")
        if verifide== password:
            artist_remove=input("what is the artist's name that you would like to remove")
            artist_scheduale.remove(artist_remove)
            loopnum-=1
            print(artist_list)
            break
        else:
            print("that is incorect")
            password_attepmt-=1

# changes schedule
def schedule_change():
    while password_attepmt <=0:
        verifide=input("what is the password?")
        if verifide== password:
            artist_change=("what is the artist that you would like to change?")
            break
        else:
            print("that is incorect")
            password_attepmt-=1
    while password_attepmt <=0:
        verifide=input("what is the password?")
        if verifide== password:
            artist_remove=input("what is the artist's name that you would like to remove")
            artist_scheduale.remove(artist_remove)
            loopnum-=1
            print(artist_list)
            break
        else:
            print("that is incorect")
            password_attepmt-=1

#changes schedule

def schedule_change():
    while password_attepmt <=0:
        verifide=input("what is the password?")
        if verifide== password:
            artist_change=("what is the artist that you would like to change?")
            break
        else:
            print("that is incorect")
            password_attepmt-=1

        

main()
