# Gavin Pierce Music Library
# This is the main file for managing your personal music library.
import random

# The list of artists and their top songs with additional information
artist_songs = {
    "Ed Sheeran": [
        {"title": "Shape of You", "year": 2017, "genre": "Pop", "album": "Divide", "length": "3:53"},
        {"title": "Perfect", "year": 2017, "genre": "Pop", "album": "Divide", "length": "4:23"},
        {"title": "Castle on the Hill", "year": 2017, "genre": "Pop", "album": "Divide", "length": "4:21"}
    ],
    "Journey": [
        {"title": "Don't Stop Believin'", "year": 1981, "genre": "Rock", "album": "Escape", "length": "4:11"},
        {"title": "Open Arms", "year": 1981, "genre": "Rock", "album": "Escape", "length": "3:19"}
    ],
    "Metallica": [
        {"title": "Enter Sandman", "year": 1991, "genre": "Heavy Metal", "album": "Metallica", "length": "5:31"},
        {"title": "Nothing Else Matters", "year": 1991, "genre": "Heavy Metal", "album": "Metallica", "length": "6:28"}
    ],
    "The Weeknd": [
        {"title": "Blinding Lights", "year": 2019, "genre": "Pop", "album": "After Hours", "length": "3:20"},
        {"title": "Save Your Tears", "year": 2020, "genre": "Pop", "album": "After Hours", "length": "3:35"}
    ]
    # Add more artists and songs as needed
}

def library_main():
    like_to_do = input_choice()

    while like_to_do != "6":  # Change to 6 to stop on option 6
        if like_to_do == "1":
            like_to_do = add_song()
        elif like_to_do == "2":
            like_to_do = remove_song()
        elif like_to_do == "3":
            like_to_do = library_search()
        elif like_to_do == "4":
            like_to_do = shuffle_song()
        elif like_to_do == "5":
            like_to_do = view_library()  # Add option to view library
        else:
            print("Invalid choice, please select again.")
            like_to_do = input_choice()

def add_song():
    artist_name = input("Enter the artist's name: ")

    # Check if the artist already exists in the library
    if artist_name in artist_songs:
        print(f"Adding a song to {artist_name}'s list.")
        song_info = get_valid_song_info()
        artist_songs[artist_name].append(song_info)
        print(f"Added '{song_info['title']}' to {artist_name}'s song list.")
    else:
        print(f"{artist_name} is not in your library.")
        add_artist = input(f"Would you like to add {artist_name} to the library? (yes/no): ").strip().lower()

        if add_artist == "yes":
            print(f"Adding {artist_name} to the library.")
            artist_songs[artist_name] = []  # Add the artist to the dictionary with an empty song list
            song_info = get_valid_song_info()  # Get the first song
            artist_songs[artist_name].append(song_info)
            print(f"Added '{song_info['title']}' to {artist_name}'s song list.")
        else:
            print(f"{artist_name} was not added.")

    return input_choice()

def remove_song():
    artist_name = input("Enter the artist's name: ")
    if artist_name in artist_songs:
        print(f"Removing a song from {artist_name}'s list.")
        song_title = input("Enter the song title to remove: ").strip()

        # Find the song in the artist's list
        song_to_remove = None
        for song in artist_songs[artist_name]:
            if song["title"].lower() == song_title.lower():
                song_to_remove = song
                break

        if song_to_remove:
            artist_songs[artist_name].remove(song_to_remove)
            print(f"Removed '{song_title}' from {artist_name}'s song list.")
        else:
            print(f"That song is not in {artist_name}'s list.")
    else:
        print("Artist not found. Please try again.")

    return input_choice()

def library_search():
    song_search = input("Enter the song name to search: ").strip().lower()
    found = False

    # Iterate through the dictionary and check each artist's list of songs
    for artist, songs in artist_songs.items():
        for song in songs:
            # Check the song name in lowercase to handle case-insensitivity
            if song["title"].lower() == song_search:
                print(f"The song '{song['title']}' by {artist} is in your library.")
                found = True
                break
        if found:
            break

    if not found:
        print(f"That song '{song_search}' is not in your library.")

    return input_choice()

def shuffle_song():
    all_songs = []
    for songs in artist_songs.values():
        all_songs.extend(songs)  # Add all songs to the list

    random.shuffle(all_songs)  # Shuffle the complete list of songs
    print("Shuffled music list (showing first 10 songs):")
    for song in all_songs[:10]:  # Show only the first 10 shuffled songs
        print(f"{song['title']} by {song['artist']}")
    
    return input_choice()

def view_library():
    print("Current Artists and Their Songs:")
    if not artist_songs:
        print("Your library is empty.")
    else:
        simple_view = input("Would you like a simple view (song title and artist) or an advanced view (all details)? (simple/advanced): ").strip().lower()
        
        for artist, songs in artist_songs.items():
            print(f"\n{artist}:")
            if simple_view == "simple":
                for song in songs:
                    print(f"  - {song['title']} by {artist}")
            elif simple_view == "advanced":
                for song in songs:
                    print(f"  - {song['title']} by {artist}, Year: {song['year']}, Genre: {song['genre']}, Album: {song['album']}, Length: {song['length']}")
            else:
                print("Invalid choice, displaying simple view.")
                for song in songs:
                    print(f"  - {song['title']} by {artist}")

    return input_choice()

def get_valid_song_info():
    song_title = input("Enter the song title: ").strip()
    year = input("Enter the year of release: ").strip()
    genre = input("Enter the genre: ").strip()
    album = input("Enter the album: ").strip()
    length = input("Enter the song length (e.g., 3:45): ").strip()

    return {
        "title": song_title,
        "year": year,
        "genre": genre,
        "album": album,
        "length": length
    }

def input_choice():
    return input("""What would you like to do? 
                     1 Add a song
                     2 Remove a song
                     3 Search for a song
                     4 Shuffle music
                     5 View all artists and songs
                     6 Stop\n""")

library_main()
