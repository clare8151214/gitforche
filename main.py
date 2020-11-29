from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=0iw3SG5WBs8')
yt.streams.first().download()