import time
import os
import SpeechManager

#change to own documents folder location
file = open("D:\\Documents\\The Witcher 3\\scriptslog.txt",'r')
file_stat = os.stat("D:\\Documents\\The Witcher 3\\scriptslog.txt")
file_size = file_stat[6]
file.seek(file_size)



while True:
    position = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(position)
    else:
        if line.startswith('[ChatMod]'):
            print(line)
            quest = line.split(':')[1]
            SpeechManager.TextToSpeech('The current quest is ' + quest.lower()) 