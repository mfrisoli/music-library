import os
import eyed3

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



names = os.listdir()
songdata = []
#print(names)

for name in names:
    print(name[-4:])
    if name[-4:] == ".mp3":

        audiofile = eyed3.load(name)
        temp = SongFile(
            filename=name,
            title=audiofile.tag.title,
            artist=audiofile.tag.artist,
            album=audiofile.tag.album,
            year=audiofile.tag.getBestDate(),
            genre=audiofile.tag.genre
        )
        songdata.append(temp)
        print(name)
#print (names)
for song in songdata:
    print(f"""
        File: {song.filename}
        Title: {song.title}
        Artist: {song.artist}
        Album: {song.album}
        Year: {song.year}
        Genre: {song.genre}""")

print(songdata)