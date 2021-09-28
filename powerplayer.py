from youtube_search import YoutubeSearch 
from playsound import playsound
import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
import re, requests, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import os
import vlc
import pafy
from time import sleep, time
import os
@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="cyan")
@click.version_option('0.1.9')
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
    video = pafy.new(url)
    length = video.length
    best = video.getbestaudio()
    
    media = vlc.MediaPlayer(best.url)
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
def add(song):
    song = " ".join(song)
    
    try:
        os.mkdir(os.path.join(os.path.expanduser("~"), ".pplay"))
    except FileExistsError as e:
        pass
    file = open(os.path.join(os.path.expanduser("~"), ".pplay", ".playlist.txt"), 'a')
    song = f'{song}\n'
    file.write(song)
@main.command('playlist', help = "Play your playlist")
def playlist():

    try:
        file = open(os.path.join(os.path.expanduser("~"), ".pplay", ".playlist.txt"), 'r')
        data = file.readlines()
 
        
        
        for line in data:
            song = line.strip()
            music_name = " ".join(song)
    
            results = YoutubeSearch(song, max_results=1).to_dict()
            res = results[0]
            url= res["url_suffix"]
            url=f'https://www.youtube.com{url}'
            title = res["title"]
            click.secho(url)
            video = pafy.new(url)
            length = video.length
            best = video.getbestaudio()
    
            media = vlc.MediaPlayer(best.url)
            click.secho(f'Playing {title}')


            media.play()
            start = time()
            while (time() - start < length):
                sleep(length - (time() - start))
    except FileNotFoundError as e:
        click.echo('Please make a playlist using the add function')
    
if __name__ == '__main__':
    main()
