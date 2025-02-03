# List of English characters
english_chars = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

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

def english_to_code():
    print("this is the english to morse code transltor.")

def code_to_english():
    print("this is the morse code to english transltor.")


def main():
    
    print("welcome to the morce code translater this program will let you translate messages in morce code and also write them too. cool right. I though so.")
    like_to_do = input("""what would you like to do? 
                       1. translate english to morse code
                       2. translate morse code to english
                       3. exit
                       """)
    if like_to_do == "1":
        english_to_code()



main()