# Powerplayer
https://pypi.org/project/powerplayer/
A python based terminal music player
Inspired by [Pauloo27](https://github.com/Pauloo27)'s [Tuner](https://github.com/Pauloo27/tuner)
## OS
Tested in Windows 10(x86_64)
Should work in MAC and Linux
## Installation
### Prerequisites

- VLC Media Player
- Python ^3.7
### Windows
Open the powershell and type
```pip install powerplayer```

### Linux/Mac
Open the terminal and type
```pip3 install powerplayer```

## Usage
After installation, type `pplay` in the terminal 
It is fine if the output is this
![image](https://user-images.githubusercontent.com/77975448/127959037-abe6f843-fafd-4f89-9c45-91d2bd6867b6.png)

### Then to play music from youtube, type
```pplay yt songname```

The output should look like this

![image](https://user-images.githubusercontent.com/77975448/125312335-cf050180-e351-11eb-9aae-2f5d20c1df9b.png)

## Powerplayer now has playlists!

### Add Command

Add Command is used to add music to playlists. It creates a playlist if one does not exist already.

The playlist is stored locally and is stored in ~/.pplay from where you can manually edit it or move it if you want

![image](https://user-images.githubusercontent.com/77975448/166191244-f4afcea0-d7fa-4f37-9577-c0f52f3e5aee.png)

### Clear Command

As the name suggests, the clear command clears your playlist

### Playlist command

Plays the songs in your playlist, in the order they were given or randomly, based on your choice
