from pynput.keyboard import Key, Listener
import SpeechToText
from nlu import get_intent


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
        if word == "Jennifer":
            word = "Yennefer"
        result += word + " "
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
    if phrase is not "":
        nluResult = get_intent(phrase)
        # print(result)
        intent = nluResult["intent"]["name"]
        entities_names = [x["value"] for x in nluResult["entities"]]
        text = nluResult["text"].lower()
        print(phrase )
        print(intent)
        print(entities_names[0])




if __name__ == '__main__':
    print("if name is main")
    main()