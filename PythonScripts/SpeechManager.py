import keyboard
from gtts import gTTS
from playsound import playsound
import sys
from MongodbScript import items, enemiesRecognised
from QueryDatabase import GetEnemyInfo, GetAlchemyInfo
from SpeechToText import RecordVoice
from W3Socket import W3socket


def LanguageUnderstanding(text):
    name = ""
    element = ""
    skip = False

    if 'quest' in text:
        mySocket = W3socket()
        mySocket.connect()
        mySocket.execute_cmd("writeCurrentQuest")
        mySocket.close()
        return

    for item in items:
        if item.lower() in text.lower():
            name = item
    if "effect" in text.lower():
        element = "effect"
    if "ingredients" in text.lower():
        element = "ingredients"

    if name is "" or element is "":
        for enemy in enemiesRecognised:
            if enemy.lower() in text.lower():
                name = enemy

        if "weak" in text.lower():
            element = "shortCombatTactic"
        if "defeat" in text.lower() or "kill" in text.lower():
            element = "longCombatTactic"
        TextToSpeech(GetEnemyInfo(name.lower(), element))
        skip = True

    if skip is False:
        TextToSpeech(GetAlchemyInfo(name.lower(), element))


def TextToSpeech(textToSay):
    print(textToSay)
    myobj = gTTS(text=textToSay, lang="en", slow=False)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')


if __name__ == '__main__':
    print("Press Q to enable microphone ")
    recording = False
    while True:
        try:
            if keyboard.is_pressed('q') and not recording:  # if key 'q' is pressed
                LanguageUnderstanding(RecordVoice())
                break
        except:
            break
