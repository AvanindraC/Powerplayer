from playsound import playsound
import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import pafy
import os
@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="cyan")
@click.version_option('0.1.1')
def main():
    """PowerPlayer - Play music in your terminal(Exclusive to windows only)"""
@main.command('setup', help = 'There are a few things to setup before using ')
@main.command('playfromyt', help = 'Play music from youtube. Give the song name')
@click.argument('song', nargs = 1)
def playfromyt(song):
    music_name = song
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for concatMusic1 in yt_title:
        pass

    click.secho(concatMusic1['content'])
    click.secho(clip2)
    video = pafy.new(clip2)
    aud = video.getbestaudio(preftype="mp3", ftypestrict=True)
    try:
        dir = os.mkdir('~\\Audio')
    except FileExistsError as e:
        dir = os.path.join('~\\Audio') 
    aud.download(dir)
    playsound(os.path.join(dir+str('\\')+yt_title+str('.mp3')))
    
    
  

@main.command('playfrompc', help = "Play an audio file in your pc")
@click.argument('dir', nargs = 1)
def playfrompc(dir):
    playsound(dir)
    
if __name__ == '__main__':
    main()