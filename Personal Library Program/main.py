# Gavin Pierce Personal Library Program

#this is the base music list
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

#this is the tuple
music_shuffel = {"Wake Up", "Take Me to the Beach", "Don't Forget Me", "Nice to Meet You", "In Your Corner",
    "Kid", "Eyes Closed", "Gods Don't Pray", "Fire in These Hills", "My Life", "Bones", "Wait for Me", 
    "Wave", "Cutthroat", "Scatter", "I'm Happy", "Lonely", "Follow You", "Giants", "Enemy", "Wrecked", 
    "Bones (Reimagined)", "Sharks", "Dull Knives (with JID)", "Crushed", "Take the World", "Daydreamer", 
    "Change",
    
    # Imagine Dragons Songs
    "It's Time", "Radioactive", "Demons", "On Top of the World", "I Bet My Life", "Whatever It Takes", 
    "Believer", "Thunder", "Natural", "Bad Liar", "Machine", "Zero", "Next to Me", "Rise Up", "Follow You", 
    "Wrecked", "Cutthroat", "Sharks", "Enemy", "Birds", "Amsterdam", "Friction", "Monster", "My Fault", 
    "Yesterday", "Round and Round", "Tiptoe", "The Fall", "I Don't Like Myself", "The River", "Walking the Wire"}

#sthis is the set for the music list
music_original = ("Wake Up", "Take Me to the Beach", "Don't Forget Me", "Nice to Meet You", "In Your Corner",
    "Kid", "Eyes Closed", "Gods Don't Pray", "Fire in These Hills", "My Life", "Bones", "Wait for Me", 
    "Wave", "Cutthroat", "Scatter", "I'm Happy", "Lonely", "Follow You", "Giants", "Enemy", "Wrecked", 
    "Bones (Reimagined)", "Sharks", "Dull Knives (with JID)", "Crushed", "Take the World", "Daydreamer", 
    "Change",
    
    # Imagine Dragons Songs
    "It's Time", "Radioactive", "Demons", "On Top of the World", "I Bet My Life", "Whatever It Takes", 
    "Believer", "Thunder", "Natural", "Bad Liar", "Machine", "Zero", "Next to Me", "Rise Up", "Follow You", 
    "Wrecked", "Cutthroat", "Sharks", "Enemy", "Birds", "Amsterdam", "Friction", "Monster", "My Fault", 
    "Yesterday", "Round and Round", "Tiptoe", "The Fall", "I Don't Like Myself", "The River", "Walking the Wire")

#this will add a song
def add_song(music_shurrel):
    print("this is the were you add a song as you now as you chose it.")
    song_name=input("what song would you like to add???? ")

    music_list.append(song_name)

    print("here is your song list now ")
    print(music_list)
    pass

def remove_song(music_shurrel):
    print("this is the were you remove a song as you now as you chose it.")
    song_name=input("what song would you like to remove???? ")

    if song_name in music_list:

        music_list.remove(song_name)
        print("here is your song list now ")
        print(music_list)

    else:
        print("that is not in the library")

        if song_name in music_list:

        music_list.remove(song_name)
        print("here is your song list now ")
        print(music_list)

    
    pass


def main():
    remove_song(music_shuffel)
    pass

main()


