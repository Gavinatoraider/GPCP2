# List of English characters
english_chars = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

# Special characters list
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '\\', '|', '~', '`']

# List of corresponding Morse code characters
morse_code = [
    '.-',    # A -> .-
    '-...',  # B -> -...
    '-.-.',  # C -> -.-.
    '-..',   # D -> -..
    '.',     # E -> .
    '..-.',  # F -> ..-.
    '--.',   # G -> --.
    '....',  # H -> ....
    '..',    # I -> ..
    '.---',  # J -> .---
    '-.-',   # K -> -.-
    '.-..',  # L -> .-..
    '--',    # M -> --
    '-.',    # N -> -.
    '---',   # O -> ---
    '.--.',  # P -> .--.
    '--.-',  # Q -> --.-
    '.-.',   # R -> .-.
    '...',   # S -> ...
    '-',     # T -> -
    '..-',   # U -> ..-
    '...-',  # V -> ...-
    '.--',   # W -> .--
    '-..-',  # X -> -..-
    '-.--',  # Y -> -.--
    '--..',  # Z -> --..
    '-----', # 0 -> -----
    '.----', # 1 -> .----
    '..---', # 2 -> ..---
    '...--', # 3 -> ...--
    '....-', # 4 -> ....-
    '.....', # 5 -> .....
    '-....', # 6 -> -....
    '--...', # 7 -> --...
    '---..', # 8 -> ---..
    '----.'  # 9 -> ----.
]

# Create dictionaries for faster lookup
english_to_morse_dict = dict(zip(english_chars, morse_code))
morse_to_english_dict = dict(zip(morse_code, english_chars))

def english_to_code():
    print("This is the English to Morse code translator.")
    english_message = input("Please enter your message (without special characters like !, @, #, etc.): ")

    # Check for special characters in the input message
    found_special_chars = [char for char in english_message if char in special_characters]
    if found_special_chars:
        print("You can't have special characters in the message.")
        return input_choice()

    # Translate to Morse code
    morse_message = ' '.join(english_to_morse_dict.get(char.upper(), '') for char in english_message if char.upper() in english_to_morse_dict)
    
    # Display the translated Morse code
    print(f"Morse Code: {morse_message}")
    return input_choice()

def code_to_english():
    print("This is the Morse code to English translator.")
    code_message = input("Please enter your Morse code message (separate symbols with spaces, e.g., .- -... .-..): ")

    # Split the message by spaces to get individual Morse code symbols
    morse_symbols = code_message.split()
    
    # Translate Morse code to English
    english_message = ''.join(morse_to_english_dict.get(symbol, '') for symbol in morse_symbols)
    
    print(f"English Message: {english_message}")
    return input_choice()

def input_choice():
    return input("""What would you like to do? 
                     1. Translate English to Morse code
                     2. Translate Morse code to English
                     3. Exit\n""")

def morse_main():
    print("Welcome to the Morse code translator! This program will let you translate messages to and from Morse code.")
    
    like_to_do = input_choice()
    
    while like_to_do != "3":
        if like_to_do == "1":
            like_to_do = english_to_code()
        elif like_to_do == "2":
            like_to_do = code_to_english()
        else:
            print("Invalid choice, please select again.")
            like_to_do = input_choice()

    print("Thanks for using the Morse code translator. Goodbye!")

# Run the main function
morse_main()
