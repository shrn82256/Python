from __future__ import unicode_literals
import youtube_dl, urllib2, re, os
from sys import argv

song_name = ' '.join(argv[1:])
suffix_list=[];	ttl_list=[]

def get_suffixes():
	srch_url = "https://www.youtube.com/results?q=" + song_name.replace(' ', '+') + "+audio"
	url_prfx = "data-context-item-id=\""
	ttl_prfx = r'" dir="ltr">';	ttl_sffx = '</a><span class'
	tm_prfx = r'aria-hidden="true">';	tm_sffx = r'</span></a> '
	pg_src = urllib2.urlopen(srch_url).read()
	strt = 0
	for x in range(len(re.findall(url_prfx, pg_src))):
		i = re.search(url_prfx + '(.{11})', pg_src[strt:])
		tm = re.search(tm_prfx + '(.*)' + tm_sffx, pg_src[strt:]).group(1) 
		ttl = re.search(ttl_prfx + '(.*)' + ttl_sffx, pg_src[strt:]).group(1)
		print x, '-->', ttl[:78], tm
		strt += i.end()
		suffix_list.append(i.group(1))
		ttl_list.append(ttl)

def get_song(url):
	ydl_opts = {
    	'format': 'bestaudio/best',
    	'outtmpl': r'~/Music/%(title)s.%(ext)s', 
    	'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
        	'preferredcodec': 'mp3',
        	'preferredquality': '192',
    	}]
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])

get_suffixes()
number = input("Song Number (-1 to exit) >>> ")
if number == -1:	exit()
os.system("clear")
print "DOWNLOADING SONG NO.", number, "\n", ttl_list[number]
print "PRESS 'Ctrl+C' TO STOP\n"
video_url = "https://www.youtube.com/watch?v=" + suffix_list[number]
get_song(video_url)

