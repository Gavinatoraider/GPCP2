#Gavin Pierce Updated Library program
import random

# List of artists and their top songs, along with song details
artist_songs = {
    "Ed Sheeran": [
        {"name": "Shape of You", "album": "Divide", "year": 2017, "genre": "Pop"},
        {"name": "Perfect", "album": "Divide", "year": 2017, "genre": "Pop"},
        {"name": "Castle on the Hill", "album": "Divide", "year": 2017, "genre": "Pop"},
        {"name": "Thinking Out Loud", "album": "X", "year": 2014, "genre": "Pop"},
        {"name": "Bad Habits", "album": "Equals", "year": 2021, "genre": "Pop"}
    ],
    "Journey": [
        {"name": "Don't Stop Believin'", "album": "Escape", "year": 1981, "genre": "Rock"},
        {"name": "Open Arms", "album": "Escape", "year": 1981, "genre": "Rock"},
        {"name": "Any Way You Want It", "album": "Departure", "year": 1980, "genre": "Rock"},
        {"name": "Faithfully", "album": "Frontiers", "year": 1983, "genre": "Rock"},
        {"name": "Separate Ways (Worlds Apart)", "album": "Frontiers", "year": 1983, "genre": "Rock"}
    ],
    "Metallica": [
        {"name": "Enter Sandman", "album": "Metallica", "year": 1991, "genre": "Heavy Metal"},
        {"name": "Nothing Else Matters", "album": "Metallica", "year": 1991, "genre": "Heavy Metal"},
        {"name": "Master of Puppets", "album": "Master of Puppets", "year": 1986, "genre": "Heavy Metal"},
        {"name": "One", "album": "And Justice for All", "year": 1988, "genre": "Heavy Metal"},
        {"name": "For Whom the Bell Tolls", "album": "Ride the Lightning", "year": 1984, "genre": "Heavy Metal"}
    ],
    "The Weeknd": [
        {"name": "Blinding Lights", "album": "After Hours", "year": 2020, "genre": "Pop"},
        {"name": "Save Your Tears", "album": "After Hours", "year": 2020, "genre": "Pop"},
        {"name": "Can't Feel My Face", "album": "Beauty Behind the Madness", "year": 2015, "genre": "Pop"},
        {"name": "Starboy", "album": "Starboy", "year": 2016, "genre": "Pop"},
        {"name": "The Hills", "album": "Beauty Behind the Madness", "year": 2015, "genre": "Pop"}
    ]
}

# Function to get valid input for song name
def get_valid_song_name():
    while True:
        song_name = input("Enter the song name: ")
        
        # Check if input is a valid string
        if song_name.isdigit():  # If input is only digits, it's considered invalid
            print("Please enter a valid song name (not just numbers).")
        elif song_name == "":  # Check if the input is empty
            print("Song name cannot be empty. Please try again.")
        else:
            return song_name  # Return the valid string input

# Function to add a song to an artist's list
def add_song():
    artist_name = input("Enter the artist's name: ")
    if artist_name in artist_songs:
        print(f"Adding a song to {artist_name}'s list.")
        song_name = get_valid_song_name()
        album_name = input(f"Enter the album for '{song_name}': ")
        song_year = input(f"Enter the year of release for '{song_name}': ")
        song_genre = input(f"Enter the genre for '{song_name}': ")
        
        artist_songs[artist_name].append({
            "name": song_name,
            "album": album_name,
            "year": int(song_year),
            "genre": song_genre
        })
        
        print(f"Added '{song_name}' to {artist_name}'s song list.")
    else:
        print("Artist not found. Please try again.")
    
    return display_menu()

# Function to remove a song from an artist's list
def remove_song():
    artist_name = input("Enter the artist's name: ")
    if artist_name in artist_songs:
        print(f"Removing a song from {artist_name}'s list.")
        song_name = get_valid_song_name()
        
        # Find the song and remove it
        for song in artist_songs[artist_name]:
            if song["name"].lower() == song_name.lower():
                artist_songs[artist_name].remove(song)
                print(f"Removed '{song_name}' from {artist_name}'s song list.")
                break
        else:
            print(f"That song is not in {artist_name}'s list.")
    else:
        print("Artist not found. Please try again.")
    
    return display_menu()

# Function to search for a song in the library
def search_song():
    song_search = get_valid_song_name().lower()  # Convert input to lowercase
    found = False
    
    # Iterate through the dictionary and check each artist's list of songs
    for artist, songs in artist_songs.items():
        for song in songs:
            if song["name"].lower() == song_search:
                print(f"The song '{song['name']}' by {artist} is in your library.")
                found = True
                break
        if found:
            break

    if not found:
        print(f"That song '{song_search}' is not in your library.")
    
    return display_menu()

# Function to shuffle all songs and display them
def shuffle_song():
    all_songs = []
    
    # Flatten the song list, adding the artist info for each song
    for artist, songs in artist_songs.items():
        for song in songs:
            song_copy = song.copy()  # Create a copy of the song details
            song_copy['artist'] = artist  # Add the artist name to the song
            all_songs.append(song_copy)

    # Shuffle the list of songs
    random.shuffle(all_songs)

    print("Shuffled music list (showing first 10 songs):")
    for song in all_songs[:10]:  # Show only the first 10 shuffled songs
        print(f"{song['name']} by {song['artist']} from {song['album']} ({song['year']}), Genre: {song['genre']}")

    return display_menu()

# Function to display the main menu
def display_menu():
    return input("""What would you like to do? 
                     1. Add a song
                     2. Remove a song
                     3. Search for a song
                     4. Shuffle music
                     5. Stop\n""")

# Main function to run the program
def main():
    print("Welcome to your music library! You can add, remove, search for songs, and shuffle your library.")
    
    action = display_menu()
    
    while action != "5":
        if action == "1":
            action = add_song()
        elif action == "2":
            action = remove_song()
        elif action == "3":
            action = search_song()
        elif action == "4":
            action = shuffle_song()
        else:
            print("Invalid choice, please select again.")
            action = display_menu()

    print("Thanks for using the music library. Goodbye!")

# Run the main function
main()
