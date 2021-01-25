import csv
import os
import eyed3
import pandas as pd

# LOAD DATA
def loadSongDataToCSV(fileNames, folderPath):
    with open("songlog.csv", "w", newline="", encoding=
    'utf-8') as f:
        fieldnames = ["filename", "title", "artist", "album", "year", "genre"]

        song_log = csv.DictWriter(f, fieldnames=fieldnames)

        song_log.writeheader()

        count = 0
        for name in fileNames:
            #print(name[-4:])
            if name[-4:] == ".mp3":

                # Load file path
                audiofile = eyed3.load(path +r"\\" + name)
        
                # Get Relevant data and add it to the log
                song_log.writerow({
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

print(f"""
    files found: {len(names)}
    MP3's loaded: {songs_loaded}
""")
# print(songdata)

for name in names:
    if name == "aaaa":
        print(name)

sub_directories = os.walk(path)

print(sub_directories)

# TRANSFORM DATA: CREATE ARTIST DIRECTORY

# Load list of all songs with PANDAS
artist_df = pd.read_csv("songlog.csv")

# Remove all Duplicates
artist_df['artist'].drop_duplicates(inplace=True)

# Remove special characters
artist_df['artist'].replace(to_replace=r'[^a-zA-Z0-9]', regex=True, value=r' ', inplace=True)

# Create directories
artist_df['artist'].to_csv("artist_log.csv")




# LOAD SONGS TO ARTIST FOLDER.