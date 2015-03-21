class song_lyric(object):
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.lyrics = ""
    def __str__(self):
        return "starts at " + self.begin + ", ends at " + self.end +", " + self.lyrics

def get_lrc(song_name, artist):
    song = ul.urlopen("http://lrc.awardspace.us/lrc/" + artist.replace(" ", "_") + "-" + song_name.replace(" ", "_") + ".lrc")
    for i in range(4):
        song.readline()
    mod = 0
    lyric_list = []
    for i in song.readlines():
        if (mod == 0):
            mod = 1
            s = song_lyric()
            s.begin = i[:10].replace("[","").replace("]","")#.replace(":","").replace(".","")
            s.lyrics = i[10:]
            lyric_list.append(s)
        else:
            mod = 0
            lyric_list[-1].end = i[:10].replace("[","").replace("]","")#.replace(":","").replace(".","")
    return lyric_list
    
ll = get_lrc("Battlefield", "Jordin Sparks")
for i in ll:
    print i

