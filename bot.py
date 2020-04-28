from pynput.keyboard import Key, Listener
import SpeechToText
from nlu import get_intent
from stateMachine import state_machine, PrepareForNewQuery
from dm import dm, initiate_priority_list, get_highest_priority_chat, remove_from_priority_list, getShortCombat
import nlg
from TextToSpeech import TextToSpeech
from PythonScripts.LogListener import *
import datetime
import random
from threading import Timer
from pygame import mixer


def on_press(key):
    global fetchingAnswer
    global phrase
    print('{0} pressed'.format(key))
    if fetchingAnswer == False and key == Key.space:
        # Stop the current message if one is active
        try:
            mixer.music.stop()
        except:
            print("No music to stop")

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
            state_machine["Entity"] = word
        if word == "Gerald" or word == "Germane" or word == "Jenna" or word == "Gerrard" or word == "Jolt" or word == "geralt":
            word = "Geralt"
            state_machine["Entity"] = word
        if word == "Siri" or word == "Cira" or word == "Circe" or word == "Cirilla" or word == "sex":
            word = "Ciri"
            state_machine["Entity"] = word
        if word == "Witch" or word == "Witches" or word == "witch" or word == "witches" or word == "there":
            word = "The Witcher"
            state_machine["Entity"] = "Witcher"
        if word == "caer" or word == "kya":
            word = "Kaer Morhen"
        if word == "orchid" or word == "orca" or word == "white":
            word = "White Orchard"
        if word == "Hydrasun" or word == "greeting" or word == "griffin":
            word = "Griffin"
        if word == "wolf" or word == "Wolf" or word == "wolfs":
            word = "Big Bad Wolf"
            state_machine["Entity"] = word
        if word == "Google":
            word = "ghoul"
            state_machine["Entity"] = word
        if word == "chill":
            word = "kill"
        if word == 'race' or word == 'rife':
            word = "wraith"
            state_machine["Entity"] = word
        if word == 'noon':
            word = "noonwraith"
            state_machine["Entity"] = word
        if word == 'tris':
            word = "triss"
            state_machine["Entity"] = word
        if word == 'by' or word == "bible" or word == "Bible":
            word == "by the well"
            state_machine["Entity"] = "devil by the well"
        if word == 'ratio' or word == 'Media' or word == 'media' or word == 'rivia' or word == 'Rivia' \
                or word == 'Radio' or word == 'radio' or word == 'review' or word == 'vidya' or word == 'rosia'\
                or word == 'river' or word == 'arrhythmia' or word == "Lydia":
            word = "rivia"
            state_machine["Entity"] = word
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
    with Listener(on_press=on_press, on_release=on_release) as listener:
        Timer(25, listener.stop).start()
        listener.join()
        print('25 seconds passed')
        return False


def main():
    global nluResult
    global phrase
    global fetchingAnswer

    current_time = datetime.datetime.now()
    previous_time = datetime.datetime.now()
    rng_cooldown = random.randint(30, 60)
    priority_list = initiate_priority_list()
    priority_list_already_used = []

    while True:
        # turned it into a loop, should work out.

        current_time = datetime.datetime.now()
        delta_time = (current_time.second + current_time.minute * 60) - (
                previous_time.second + previous_time.minute * 60)

        # print("hello world")
        # TODO: method to put the current state to the previous state

        if rng_cooldown < delta_time:
            print("The random cooldown is over, the chatbot will now say either some edgy chitchat "
                  "or talk about the game ")
            previous_time = current_time
            # testing values, this is the duration between two chitchat lines
            rng_cooldown = random.randint(5, 15)

            # testing value, this represent the likehood of the bot saying a chitchat line or talk about the game
            if random.randint(0, 100) > 100:
                # update_W3_data()
                W3_data = get_W3_data()

                if W3_data.current_quest != "":
                    priority_list[3].append(W3_data.current_quest)
                    print(priority_list[3])
                if W3_data.current_objective != "":
                    priority_list[2].append(W3_data.current_objective)
                    print(priority_list[2])

                if len(W3_data.near_monsters) > 0:
                    if len(W3_data.near_monsters) > 0:
                        monster = W3_data.near_monsters[0]["name"]
                        monster_tactic = getShortCombat(monster)
                        if monster_tactic != "Entry invalid":
                            priority_list[1].append(monster_tactic)

                if W3_data.geralt_health != "":
                    if W3_data.geralt_health < 25:
                        health_sentence = "Don't be stubborn and get to safety. Live to fight another day"
                        if health_sentence not in priority_list[0]:
                            priority_list[0].append(health_sentence)

                # gotta add more stuff in it.

                # Get the highest priority chat & send it to the TTS (NGL work was done before adding the elements
                # Into the list)
                sentence = get_highest_priority_chat(priority_list)
                if sentence in priority_list_already_used:
                    if sentence != "Hummm":
                        remove_from_priority_list(priority_list, sentence)
                        sentence = get_highest_priority_chat(priority_list)

                priority_list_already_used.append(sentence)
                TextToSpeech(sentence)

                # TextToSpeech("Hummm")
            else:
                state_machine["Intent"] = "Chitchat"
                state_machine["Entity"] = "Narrator"
                state_machine["Phrase"] = ""
                chitchat_sentence = nlg.NLG(state_machine)
                TextToSpeech(chitchat_sentence.ChitChat())

        else:
            fetchingAnswer = False
            CheckKeys()

            if phrase is not "":

                nluResult = get_intent(phrase)
                # print(result)
                intent = nluResult["intent"]["name"]
                entities_names = [x["value"] for x in nluResult["entities"]]
                text = nluResult["text"].lower()

                # tries to retrieve the entity of the previous user input and store it as Previous entity
                """
                try:
                    state_machine["P_Entity"] = state_machine["Entity"]
                except AttributeError:
                    text = "none"
                """

                # Checks if this sentence wasn't already processed
                if (text != state_machine["P_Phrase"]):

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
                    print("state_machine before DM: ", state_machine)
                    print("\n")
                    info = dm()

                    # tries to fill the state machine with the new information retrieved from the DB or the game
                    try:
                        state_machine["Info"] = info
                    except AttributeError:
                        info = "none"

                    # for testing purposes
                    print("state_machine after DM : ", state_machine)
                    print("\n")
                    print("info : ", info)

                    # nlg

                    final_phrase = nlg.NLG(state_machine)
                    answer = final_phrase.get_nlg()
                    previous_time = datetime.datetime.now()
                    TextToSpeech(answer)
                    PrepareForNewQuery()



if __name__ == '__main__':
    print("if name is main")
    main()
