import urllib2 as ul
import pyttsx
import time
from muse_get_lrc import *


def get_time_diff(start, end):
    s = int(start[0:2])*60 + int(start[2:4]) + float(start[4:])/100
    e = int(end[0:2])*60 + int(end[2:4]) + float(end[4:])/100
    return e-s

def sing_song(song_name, artist):
    engine = pyttsx.init()
    engine.setProperty('rate', engine.getProperty('rate')-100)

    lyric_list = get_lrc(song_name, artist)
    for i in xrange(len(lyric_list) - 1):
        length = get_time_diff(lyric_list[i].begin, lyric_list[i].end)
        diff = get_time_diff(lyric_list[i].begin, lyric_list[i+1].begin)
        start = time.time()
        print "length:", length
        print "diff:", diff
        words = lyric_list[i].lyrics
        
        engine.setProperty('rate', int(len(words.split())*60/length))
        engine.say(words)
        engine.runAndWait()
        td = time.time() - start
        if length < diff:
            pass #time.sleep(diff-length)
    engine.say(lyric_list[-1].lyrics)
    engine.runAndWait()

sing_song("Love Story", "Taylor Swift")