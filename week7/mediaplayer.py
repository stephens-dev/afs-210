import random

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        


def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")
artist = ["ACDC", "Alan Jackson",'Hollywood Undead', 'miricleofsound ']
songs = ['Highway to Hell', 'Old Red', 'For the Glory', 'Wake the White Wolf']
i = 0
playing = songs[i]
index = 0
while True:
    
    menu()
    choice = int(input())

    if choice == 1:
        print("Song name:")
        songs.append(str(input()))
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        print("New Song Added to Playlist")
    elif choice == 2:
        print("What is the song")
        songs.remove(str(input()))
        
        print("Song Removed to Playlist")
    elif choice == 3:
        print("Playing....")        
        print(songs[0])
        # Play the playlist from the beginning
        # Display song name that is currently playing
    elif choice == 4:
        songs.append(songs[0])
        songs.pop(0)
        print(playing)
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")    
                     
    elif choice == 5:
        last = songs.pop(-1)
        songs.insert(0, last) 
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
    elif choice == 6:
        random.shuffle(songs)
        random.shuffle(artist)
        print(songs)
        print(artist)
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        print(songs)
        # Show the current song list order
        # print("\nSong list:\n")
    elif choice == 0:
        print("Goodbye.")
        break

            
