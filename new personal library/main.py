# Gavin Pierce Music Library
# This is the main file for managing your personal music library.
import random

# The list of artists and their top songs
artist_songs = {
    "Ed Sheeran": [
        "Shape of You", "Perfect", "Castle on the Hill", "Thinking Out Loud", "Bad Habits", "Galway Girl"
    ],
    "Journey": [
        "Don't Stop Believin'", "Open Arms", "Any Way You Want It", "Faithfully", "Separate Ways (Worlds Apart)", "Lights"
    ],
    "Metallica": [
        "Enter Sandman", "Nothing Else Matters", "Master of Puppets", "One", "The Unforgiven", "For Whom the Bell Tolls"
    ],
    "The Weeknd": [
        "Blinding Lights", "Save Your Tears", "Can't Feel My Face", "Starboy", "The Hills", "In the Night"
    ],
    "Imagine Dragons": [
        "Wake Up", "Take Me to the Beach", "Don't Forget Me", "Nice to Meet You", "In Your Corner", "Kid", 
        "Eyes Closed", "Gods Don't Pray", "Fire in These Hills", "My Life", "Bones", "Wait for Me", "Wave", 
        "Cutthroat", "Scatter", "I'm Happy", "Lonely", "Follow You", "Giants", "Enemy", "Wrecked", 
        "Bones (Reimagined)", "Sharks", "Dull Knives (with JID)", "Crushed", "Take the World", "Daydreamer", 
        "Change", "It's Time", "Radioactive", "Demons", "On Top of the World", "I Bet My Life", "Whatever It Takes", 
        "Believer", "Thunder", "Natural", "Bad Liar", "Machine", "Zero", "Next to Me", "Rise Up", "Birds", 
        "Amsterdam", "Friction", "Monster", "My Fault", "Yesterday", "Round and Round", "Tiptoe", "The Fall", 
        "I Don't Like Myself", "The River", "Walking the Wire"
    ],
    "Taylor Swift": [
        "Love Story", "You Belong with Me", "Shake It Off", "Blank Space", "All Too Well", "Cardigan", 
        "Look What You Made Me Do", "Delicate", "Style", "Wildest Dreams", "Lover", "Enchanted", 
        "Red", "Tim McGraw", "Mine", "Back to December"
    ],
    "Adele": [
        "Someone Like You", "Rolling in the Deep", "Hello", "Set Fire to the Rain", "Skyfall", "When We Were Young",
        "Chasing Pavements", "Make You Feel My Love", "Turning Tables", "Water Under the Bridge", "Rumour Has It"
    ],
    "Billie Eilish": [
        "Bad Guy", "Everything I Wanted", "Ocean Eyes", "Bury a Friend", "When the Party's Over", 
        "No Time to Die", "You Should See Me in a Crown", "Therefore I Am", "All the Good Girls Go to Hell", 
        "My Future", "Wish You Were Gay"
    ],
    "Coldplay": [
        "Yellow", "Fix You", "Viva la Vida", "The Scientist", "Clocks", "Paradise", "Hymn for the Weekend", 
        "A Sky Full of Stars", "Adventure of a Lifetime", "In My Place", "Magic", "Something Just Like This", 
        "Shiver", "Speed of Sound", "Everglow"
    ],
    "Drake": [
        "Hotline Bling", "God's Plan", "In My Feelings", "Started from the Bottom", "One Dance", "Take Care", 
        "Nice for What", "Nonstop", "Hotline Bling", "Marvins Room", "Passionfruit", "Headlines", 
        "Laugh Now Cry Later", "Controlla", "The Ride"
    ]
}

def main():
    like_to_do = input_choice()
    
    while like_to_do != "6":
        if like_to_do == "1":
            like_to_do = add_song()
        elif like_to_do == "2":
            like_to_do = remove_song()
        elif like_to_do == "3":
            like_to_do = library_search()
        elif like_to_do == "4":
            like_to_do = shuffle_song()
        elif like_to_do == "5":
            like_to_do = view_library()
        else:
            print("Invalid choice, please select again.")
            like_to_do = input_choice()

def add_song():
    artist_name = input("Enter the artist's name: ")
    
    # Check if the artist already exists in the library
    if artist_name in artist_songs:
        print(f"Adding a song to {artist_name}'s list.")
        song_name = get_valid_song_name()
        artist_songs[artist_name].append(song_name)
        print(f"Added '{song_name}' to {artist_name}'s song list.")
    else:
        print(f"{artist_name} is not in your library.")
        add_artist = input(f"Would you like to add {artist_name} to the library? (yes/no): ").strip().lower()
        
        if add_artist == "yes":
            print(f"Adding {artist_name} to the library.")
            artist_songs[artist_name] = []  # Add the artist to the dictionary with an empty song list
            song_name = get_valid_song_name()  # Get the first song
            artist_songs[artist_name].append(song_name)
            print(f"Added '{song_name}' to {artist_name}'s song list.")
        else:
            print(f"{artist_name} was not added.")
    
    return input_choice()

def remove_song():
    artist_name = input("Enter the artist's name: ")
    if artist_name in artist_songs:
        print(f"Removing a song from {artist_name}'s list.")
        song_name = get_valid_song_name()
        
        if song_name in artist_songs[artist_name]:
            artist_songs[artist_name].remove(song_name)
            print(f"Removed '{song_name}' from {artist_name}'s song list.")
        else:
            print(f"That song is not in {artist_name}'s list.")
    else:
        print("Artist not found. Please try again.")
    
    return input_choice()

def library_search():
    song_search = get_valid_song_name().lower()  # Convert input to lowercase
    found = False
    
    # Iterate through the dictionary and check each artist's list of songs
    for artist, songs in artist_songs.items():
        for song in songs:
            # Check the song name in lowercase to handle case-insensitivity
            if song.lower() == song_search:
                print(f"The song '{song}' by {artist} is in your library.")
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
    print(all_songs[:10])  # Show only the first 10 shuffled songs
    
    return input_choice()

def view_library():
    print("Current Artists and Their Songs:")
    if not artist_songs:
        print("Your library is empty.")
    else:
        for artist, songs in artist_songs.items():
            print(f"{artist}:")
            for song in songs:
                print(f"  - {song}")
    return input_choice()

def get_valid_song_name():
    while True:
        song_name = input("Enter the song name: ").strip()
        
        # Check if input is a valid string
        if song_name.isdigit():  # If input is only digits, it's considered invalid
            print("Please enter a valid song name (not just numbers).")
        elif song_name == "":  # Check if the input is empty
            print("Song name cannot be empty. Please try again.")
        else:
            return song_name  # Return the valid string input

def input_choice():
    return input("""What would you like to do? 
                     1 Add a song
                     2 Remove a song
                     3 Search for a song
                     4 Shuffle music
                     5 View all artists and songs
                     6 Stop\n""")

main()
