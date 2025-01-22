# Jackson Hauley, Gavin Pierce, Lizzy Saldana, Luke Murdock

# Initializing Variables
artist_list = []
# Defining Funcitons

def main():
    while True:
        cs()
        choice = int_input("MUSIC FESTIVAL\n\n1. Information\n2. Tickets\n3. Schedule\n4. Artists\n5. Recommendation\n6. Exit")
        if choice == 1: # Information
            pass
        elif choice == 2: # Buy Tickets
            pass
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