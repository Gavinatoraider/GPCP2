import random

# Base music list
music_list = [
    "Wake Up", "Take Me to the Beach", "Don't Forget Me", "Nice to Meet You", "In Your Corner",
    "Kid", "Eyes Closed", "Gods Don't Pray", "Fire in These Hills", "My Life", "Bones", "Wait for Me", 
    "Wave", "Cutthroat", "Scatter", "I'm Happy", "Lonely", "Follow You", "Giants", "Enemy", "Wrecked", 
    "Bones (Reimagined)", "Sharks", "Dull Knives (with JID)", "Crushed", "Take the World", "Daydreamer", 
    "Change",

    # Imagine Dragons Songs
    "It's Time", "Radioactive", "Demons", "On Top of the World", "I Bet My Life", "Whatever It Takes", 
    "Believer", "Thunder", "Natural", "Bad Liar", "Machine", "Zero", "Next to Me", "Rise Up", "Follow You", 
    "Wrecked", "Cutthroat", "Sharks", "Enemy", "Birds", "Amsterdam", "Friction", "Monster", "My Fault", 
    "Yesterday", "Round and Round", "Tiptoe", "The Fall", "I Don't Like Myself", "The River", "Walking the Wire"
]

# Function to get a valid song name (ensures string input)
def get_valid_song_name():
    while True:
        song_name = input("Enter the song name: ")
        
        # Check if input is a valid string, reject if it's an integer or doesn't fit expectations
        if song_name.isdigit():  # If input is only digits, it's considered invalid
            print("Please enter a valid song name (not just numbers).")
        elif song_name == "":  # Check if the input is empty
            print("Song name cannot be empty. Please try again.")
        else:
            return song_name  # Return the valid string input

# This will add a song
def add_song():
    print("This is where you add a song to your list.")
    song_name = get_valid_song_name()  # Get a valid song name from the user

    music_list.append(song_name)

    print("Here is your song list now:")
    print(music_list)

# Removes song from list
def remove_song():
    print("This is where you remove a song from your list.")
    song_name = get_valid_song_name()  # Get a valid song name from the user

    if song_name in music_list:
        music_list.remove(song_name)
        print("Here is your song list now:")
        print(music_list)
    else:
        print("That song is not in the library.")

# Searches library for song (case insensitive)
def library_search():
    song_search = get_valid_song_name().lower()  # Convert input to lowercase
    
    found = False
    for song in music_list:
        if song.lower() == song_search:
            print(f"The song '{song}' is in your library.")
            found = True
            break
    
    if not found:
        print(f"That song '{song_search}' is not in your list.")

# Shuffle and display shuffled music list
def shuffle_song():
    shuffled_music = list(music_list)  # Use music_list, not music_shuffle
    random.shuffle(shuffled_music)      # Shuffle the list
    print("Shuffled music list:")
    print(shuffled_music)

def main():
    while True:
        print("\nWelcome to the Music Library! Please choose an option:")
        print("1. Add a song")
        print("2. Remove a song")
        print("3. Search for a song")
        print("4. Shuffle music")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        # Ensure the choice is a valid integer
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        if choice == 1:
            add_song()
        elif choice == 2:
            remove_song()
        elif choice == 3:
            library_search()
        elif choice == 4:
            shuffle_song()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
