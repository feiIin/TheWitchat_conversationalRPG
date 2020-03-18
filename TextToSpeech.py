from gtts import gTTS
from playsound import playsound

def TextToSpeech(textToSay):
    print(textToSay)
    myobj = gTTS(text=textToSay, lang="en", slow=False)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')