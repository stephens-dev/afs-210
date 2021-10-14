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
        
class Player:
    def __init__(self):
        self.songs = []

    def addSong(self, song):
        self.songs.append(song)
    
    def removeSong(self, song):
        
        for i in self.songs:
            if song == i.getTitle():
                self.songs.remove(i)
                break
    
    def skipSong(self):
        self.songs.append(self.songs[0])
        self.songs.pop(0)

    def prevSong(self):
        last = self.songs.pop(-1)
        self.songs.insert(0, last)
    
    

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

player = Player()
song1 = Song('Highway to Hell','ACDC')
song2 = Song('OLd Red','Alan Jackson')
song3 = Song('Rise','State of Mine')
song4 = Song('Oh my Son','Peyton Perrish')
player.addSong(song1)
player.addSong(song2)
player.addSong(song3)
player.addSong(song4)

while True:
    
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        
        print("Song name:")
        song_name = (str(input()))

        print("Song aritst:")
        song_artist = (str(input()))

        song = Song(song_name, song_artist)
        player.addSong(song)

        print("New Song Added to Playlist")

    elif choice == 2:
        print("What is the song")

        player.removeSong(str(input()))

        print("Song Removed to Playlist")
    elif choice == 3:
        # Display song name that is currently playing
        # Play the playlist from the beginning

        print("Playing....")        
        print(player.songs[0].getTitle())
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing

        player.skipSong()
        print("Skipping....")    
        
                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing

        player.prevSong()
        print("Replaying....")  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing

        random.shuffle(player.songs)
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song

        print(player.songs[0])
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        # Show the current song list order
        # print("\nSong list:\n")
        
        for i in player.songs:
            print(str(i))
        
    elif choice == 0:
        print("Goodbye.")
        break

            
