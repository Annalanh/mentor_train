import json
from youtube_dl import YoutubeDL
from pyglet.media import Source, Player, load
import pyglet



option = [
    {'1' : 'Show all songs'},
    {'2' : 'Show show detail'},
    {'3' : 'Play a song'},
    {'4' : 'Search and download a song'},
    {'5' : 'Exit'}
]

List = []
datasong = []

while True:
    for i in option:
        for key, value in i.items():
            print(key, '.', value)
    opt = int(input("Your choice: "))

    if opt == 1:
        with open('songs.json', encoding = 'utf-8') as data:
            song = json.loads(data.read())
        if song == []:
            print("Empty list!")
        else:
            for index, music in enumerate(song):
                print(index + 1, ' - ', music['title'])

    elif opt == 2:
        with open('songs.json', encoding = 'utf-8') as data:
            song = json.loads(data.read())
        for index, music in enumerate(song):
            print(index + 1, ' - ', music['title'])
        info = int(input("Index of the song: "))

        found = False
        songFound = {}
        for i in range(len(song)):
            if i == info - 1:
                found = True
                songFound = song[info - 1]
        
        if found == True:
            print(songFound['id'], " ", songFound['webpage_url'])
        else:
            print("Not found")

    elif opt == 3:
        with open('songs.json', encoding = 'utf-8') as data:
            song = json.loads(data.read())
        for index, music in enumerate(song):
            print(index + 1, " - ", music['title'])

        if song == []:
            print("Empty list")
        else:
            play_song = int(input("Song to play: "))
            mp3File = song[play_song - 1]['id'] + '.mp3'

            player = Player()
            source = load(mp3File)
            player.queue(source)
            player.play()
            while True:
                interact = (input("play, pause or stop:"))
                if interact == "play":
                    player.play()
                elif interact == "pause":
                    player.pause()
                elif interact == "stop":
                    player.pause()
                    break
    
    elif opt == 4:
        with open('songs.json', encoding = 'utf-8') as data:
            song = json.loads(data.read())
        
        datasong = song

        search = input("Search song: ")

        optionsExtract = {
            'default_search' : 'ytsearch3'
        }

        ydl = YoutubeDL(optionsExtract)
        searched = ydl.extract_info(search, download = False)
        List = searched['entries']

        optionsDownload = {
            'outtmpl' : '%(id)s',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }]
        }

        for index, music in enumerate(List):
            print(index + 1, " - ", music['title'])
        
        download = int(input("Choose the song to down: "))

        ydl1 = YoutubeDL(optionsDownload)
        downloaded = ydl1.extract_info(List[download - 1]['id'], download = True)

        datasong.append(downloaded)
        with open('songs.json', 'w')as d:
            json.dump(datasong, d)
    
    elif opt == 5:
        break