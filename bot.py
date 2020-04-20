from pynput.keyboard import Key, Listener
import SpeechToText
from nlu import get_intent
from stateMachine import state_machine
from dm import dm
import nlg
from TextToSpeech import TextToSpeech

def on_press(key):
    global fetchingAnswer
    global phrase
    print('{0} pressed'.format(key))
    if fetchingAnswer == False and key ==  Key.space:
        print("LOOK FOR PHRASE")
        phrase = cleanUpPhrase(SpeechToText.RecordVoice())
        print("GOT PHRASE")
        fetchingAnswer = True
    return False

# TODO: add more cleaning, for all words that need to be cleaned
def cleanUpPhrase(text):
    print("This is cleanUp ")
    result = ""
    split = text.split()
    for word in split:
        if word == "Jennifer" or word == "yennefer" or word == "Yanni" or word == "Jonathan " or word == "Jenny":
            word = "Yennefer"
        if word == "Gerald" or word == "Germane" or word == "Jenna" or word == "Gerrard":
            word = "Geralt"
        if word == "Siri" or word == "Cira" or word == "Circe" or word == "Cirilla":
            word = "Ciri"
        if word == "Witch" or word == "Witches" or word == "witch" or word == "witches" or word == "there":
            word = "The Witcher"
        if word == "caer" or word == "kya":
            word = "Kaer Morhen"
        if word == "orchid" or word == "orca" or word == "white":
            word = "White Orchard"
        if word == "Hydrasun" or word == "greeting" or word == "griffin":
            word = "Griffin"
        if word == "wolf" or word == "Wolf" or word == "wolfs":
            word = "Big Bad Wolf"
        result += word + " "
    print("This is the new phrase: " + result)
    return result

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

fetchingAnswer = False
phrase = ""
nluResult = ""
def CheckKeys():
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()



def main():
    global nluResult
    global phrase
    CheckKeys()
    #print("hello world")
    # TODO: method to put the current state to the previous state

    if phrase is not "":
        nluResult = get_intent(phrase)
        # print(result)
        intent = nluResult["intent"]["name"]
        entities_names = [x["value"] for x in nluResult["entities"]]
        text = nluResult["text"].lower()

        # tries to retrieve the entity of the previous user input and store it as Previous entity
        try:
            state_machine["P_Entity"] = state_machine["Entity"]
        except AttributeError:
            text = "none"

        # tries to fill the state machine with the Intent of the new phrase
        try:
            state_machine["Intent"] = intent
        except AttributeError:
            intent = "none"

        # tries to fill the state machine with the Entity of the new phrase
        try:
            state_machine["Entity"] = entities_names[0]
        except IndexError:
            entity = "none"

        # tries to fill the state machine with the new phrase
        try:
            state_machine["Phrase"] = text
        except AttributeError:
            text = "none"

        print("\n")
        info = dm()

        # tries to fill the state machine with the new information retrieved from the DB or the game
        try:
            state_machine["Info"] = info
        except AttributeError:
            info = "none"

        # nlg
        final_phrase = nlg.NLG(state_machine)
        answer = final_phrase.get_nlg()
        TextToSpeech(answer)


if __name__ == '__main__':
    print("if name is main")
    main()