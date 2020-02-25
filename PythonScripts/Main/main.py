import keyboard
from gtts import gTTS
from playsound import playsound

from MongodbScript import items, enemiesRecognised
from QueryDatabase import GetEnemyInfo, GetAlchemyInfo
from SpeechToText import RecordVoice

# THIS IS A TEMPORARY LNU
# This function takes text (string) as a parameter, it then checks to see if there are key words found in the string
# These keywords match with the elements in the database and the name of the Enemy or Items found in the respective
# Arrays in the QueryDatabse Script
def LanguageUnderstanding(text):
    name = ""
    element = ""
    skip = False
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


# This function changes text to speech, it takes a string as a parameter. The text is then sent to Google Text To speech
# Google then returns an MP3 file with the text said to speech. We save this MP3 file and then autoplay it.
def TextToSpeech(textToSay):
    print(textToSay)
    myobj = gTTS(text=textToSay, lang="en", slow=False)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')

# This is the main method of our project. it asks for the user to press the Q button, once that's done it calls the
# RecordVoice function which is found in the SpeechToText script, it then sends the string that that function returns
# To the (Temporary) LanguageUnderstanding function.
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
