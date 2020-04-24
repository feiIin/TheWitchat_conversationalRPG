from gtts import gTTS
from pygame import mixer


count = 0;
def TextToSpeech(textToSay):
    global count

    print(textToSay)
    myobj = gTTS(text=textToSay, lang="en", slow=False)
    myobj.save(f'welcome_{count % 2}.mp3')
    # playsound(filename)
    mixer.init()
    mixer.music.load(f'welcome_{count % 2}.mp3')
    mixer.music.play()
    count += 1

