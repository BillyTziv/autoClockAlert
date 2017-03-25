#!/bin/python
from time import sleep
from gtts import gTTS
import os

# This script alerts user when time is 12, 1, 2, 3, 4 etc...

while(1):
    os.system("date +'%I:%M' > tmp")
    out = open('tmp', 'r').read()
    out = out.strip().replace('0', '')
    data = out.split(":")
    out = data[0] + "o'clock"
    if (data[1] == "00"):
        print "Lets hear something!"
        tts=gTTS(text=out, lang='en')
        tts.save('time.mp3')

        os.system('mpv --no-video time.mp3')
        os.system("remove time.mp3")
    else:
        print "Waiting..."
    sleep(60)
