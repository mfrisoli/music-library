import os
import eyed3
import csv

class SongFile:
    """
    Family based on main parameters from a .mp3 file
    """
    def __init__(self, filename, title, artist, album, year, genre):
        self.filename = filename
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre

def loadSongDataToCSV(fileNames, folderPath):
    with open("songlog.csv", "w", newline="") as f:
        fieldnames = ["filename", "title", "artist", "album", "year", "genre"]

        songLog = csv.DictWriter(f, fieldnames=fieldnames)

        songLog.writeheader()

        count = 0
        for name in fileNames:
            #print(name[-4:])
            if name[-4:] == ".mp3":

                # Load file path
                audiofile = eyed3.load(path +r"\\" + name)
        
                # Get Relevant data and add it to the log
                songLog.writerow({
                    'filename': name,
                    'title': audiofile.tag.title,
                    'artist': audiofile.tag.artist,
                    'album': audiofile.tag.album,
                    'year': audiofile.tag.getBestDate(),
                    'genre': audiofile.tag.genre
                })
                count += 1
    return count



# Set eyed3 log levels to error only
eyed3.log.setLevel("ERROR")

path = r'E:\Music'
#path = r"C:\Users\marco\code\music-library\.test_files"
names = os.listdir(path)

songs_loaded = loadSongDataToCSV(fileNames=names, folderPath=path)


#print(names)
#for name in names:
#    #print(name[-4:])
#    if name[-4:] == ".mp3":
#        
#        audiofile = eyed3.load(path +r"\\" + name)
#        
#        temp = SongFile(
#            filename=name,
#            title=audiofile.tag.title,
#            artist=audiofile.tag.artist,
#            album=audiofile.tag.album,
#            year=audiofile.tag.getBestDate(),
#            genre=audiofile.tag.genre
#        )
#        songdata.append(temp)
#        count += 1
        #print(name)
#print (names)
#for song in songdata:
#    print(f"""
#        File: {song.filename}
#        Title: {song.title}
#        Artist: {song.artist}
#        Album: {song.album}
#        Year: {song.year}
#        Genre: {song.genre}""")

print(f"""
    files found: {len(names)}
    MP3's loaded: {songs_loaded}
""")
# print(songdata)

for name in names:
    if name == "aaaa":
        print(name)