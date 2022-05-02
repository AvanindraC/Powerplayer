from youtube_search import YoutubeSearch 
from playsound import playsound
import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
import re, requests, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import os
import vlc
import youtube_dl
from time import sleep, time
import os
import random
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'tmp/%(id)s.%(ext)s',
    'noplaylist': True,
    'quiet': True,
    'prefer_ffmpeg': True,
    'audioformat': 'mp3',
    'forceduration':True}

@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="cyan")
@click.version_option('0.2.0')
def main():
    """PowerPlayer - Play music in your terminal"""
@main.command('yt', help = 'Play music from youtube. Give the song name')
@click.argument('song', nargs = -1)
def playfromyt(song):
    music_name = " ".join(song)
    
    
    results = YoutubeSearch(music_name, max_results=1).to_dict()
    res = results[0]
    url= res["url_suffix"]
    url=f'https://www.youtube.com{url}'
    title = res["title"]
    click.secho(url)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(
        url, download=False)
        urll = info['formats'][0]['url']
        length=info['duration']
    
    media = vlc.MediaPlayer(urll)
    click.secho(f'Playing {title}')


    media.play()
    start = time()
    while (time() - start < length):
        sleep(length - (time() - start))
        a = click.prompt('Enter your next song or press Ctrl+C to exit')
        playfromyt(a)
    
@main.command('clear', help="clear your playlist") 
def clear():
    file = open(os.path.join(os.path.expanduser("~"), ".pplay", ".playlist.txt"), 'w')
    file.write(' ')
@main.command('add', help = "Add a song to your playlist")
@click.argument('song', nargs = -1)
@click.option('--playlist', '-p', nargs = 1)
def add(song, playlist):
    
    try:
        os.mkdir(os.path.join(os.path.expanduser("~"), ".pplay"))
    except FileExistsError as e:
        pass
    file = open(os.path.join(os.path.expanduser("~"), ".pplay", f".{playlist}.txt"), 'a')
    song = f'{song}\n'
    file.write(song)
    click.secho(f'{song} has been added to {playlist}')
@main.command('playlist', help = "Play your playlist")
@click.argument('playlistname', nargs = 1)
@click.option('--shuffle','-s', nargs=1)
def playlist(playlistname, shuffle="False"):

    try:
        file = open(os.path.join(os.path.expanduser("~"), ".pplay", f".{playlistname}.txt"), 'r')
        data = file.readlines()
        shuffle=shuffle.lower()
        if shuffle == True:
            
            data=random.choice(data)
            
            
            
               
            results = YoutubeSearch(data, max_results=1).to_dict()
            res = results[0]
            url= res["url_suffix"]
            url=f'https://www.youtube.com{url}'
            title = res["title"]
            
            click.secho(data)
            
            click.secho(url)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(
                url, download=False)
                urll = info['formats'][0]['url']
                length=info['duration']
    
            media = vlc.MediaPlayer(urll)
            click.secho(f'Playing {title}')

            media.play()
            start = time()
            while (time() - start < length):
                sleep(length - (time() - start))
        else:
            results = YoutubeSearch(data, max_results=1).to_dict()
            res = results[0]
            url= res["url_suffix"]
            url=f'https://www.youtube.com{url}'
            title = res["title"]
            click.secho(res)
            
            click.secho(url)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(
                url, download=False)
                urll = info['formats'][0]['url']
                length=info['duration']
    
            media = vlc.MediaPlayer(urll)
            click.secho(f'Playing {title}')


            media.play()
            start = time()
            while (time() - start < length):
                sleep(length - (time() - start))

    except FileNotFoundError as e:
        click.echo('Please make a playlist using the add function')
    
if __name__ == '__main__':
    main()
