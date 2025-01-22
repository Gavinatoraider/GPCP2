# Jackson Hauley, Gavin Pierce, Lizzy Saldana, Luke Murdock

# Initializing Variables

# Defining Funcitons

def main():
    while True:
        cs()
        choice = int_input("MUSIC FESTIVAL\n\n1. Information\n2. Tickets\n3. Schedule\n4. Recommendation\n5. Exit")
        if choice == 1: # Information
            pass
        elif choice == 2: # Buy Tickets
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
    
def cs(): # Clear Screen
    print("\033c",end="")

# Running Code

main()