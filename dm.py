'''
Method/info needed from the DB
(look to lore/action/ingredient/monster.txt files to see what are the possible values)

Related to lore.txt values

getWhoIsEntity(value)
getWhereIsEntity(value)
getInfoAboutEntity(value)
getRelationshipBetweenGeraltAndEntity(value)
getFactsAboutEntity(value) # e.g. What happened at [White Orchard] or tell me more about x

Related to ingredient.txt

getHowToCraftEntity(value)
getWhereToFindEntity(value)
getWhatToDoWithEntity(value)
getWhatIsPossibleToCraftNow(value) # for the game not DB
isPossibleToCraftEntity(value) # for game, boolean

Related to monster.txt

getWhatIsEntity(value)
getWhatIsThisEntity(value) # for game not DB
getWeaknessesOfEntity(value)
getLocationOfMonster(value) # e.g. Where can I fight a [Griffin](monster)?

Related to action.txt

This are examples of possible questions:

- Should we [follow the tracks](action) ?
- Do I need to [follow the tracks](action) ?
- Do we need to [talk to villager](action) ?
- Should I [talk to Tomira](action) ?
- Do we need to [kill the griffon](action) ?
- Should I [kill the wild dogs](action) ?

How to answer to them? DO you think we can grab some info from the DB / Game / we hard code them?

########################################################
Methods in string:

getWhoIsEntity()
getWhereIsEntity()
getInfoAboutEntity()
getRelationshipBetweenGeraltAndEntity()
getFactsAboutEntity()

Related to ingredient.txt

getHowToCraftEntity()
getWhereToFindEntity()
getWhatToDoWithEntity()
getWhatIsPossibleToCraftNow()
isPossibleToCraftEntity() # boolean

Related to monster.txt

getWhatIsEntity()
getWhatIsThisEntity()
getWeaknessesOfEntity()
getLocationOfMonster()

unknown()

'''
from PythonScripts import ConnectToDatabase
from nlu import get_intent
from stateMachine import state_machine
from MongodbScript import *


# RULES ##############################


def get_info(intent, text, entity):
    # it the system is not able to get an intent, no info will be retrieved.
    if intent == "none" or entity == "none":
        print("I DID IT")
        state_machine["Method"] = "unknown()"
        return ""

    # get_lore intent #
    if intent == "get_lore":
        if text.find("where") != -1:
            state_machine["Method"] = "getWhereIsEntity()"
            return getWhereIsEntity(entity)

        if text.find("what") != -1:
            state_machine["Method"] = "getWhatIsEntity()"
            return getWhatIsEntity(entity)

        elif text.find("who") != -1:
            state_machine["Method"] = "getWhoIsEntity()"
            return getWhoIsEntity(entity)

        elif text.find("you") != -1 or text.find("between") != -1:
            state_machine["Method"] = "getRelationshipBetweenGeraltAndEntity()"
            return getRelationshipBetweenGeraltAndEntity(entity)

        elif text.find("more") != -1 or text.find("tell") != -1:
            state_machine["Method"] = "getFactsAboutEntity()"
            return getFactsAboutEntity(entity)

        else:
            state_machine["Method"] = "unknown()"
            return None

    # craft_helper intent #
    if intent == "craft_helper":
        if text.find("how") != -1 and text.find("can") != -1 or text.find("how") != -1 and text.find("do") != -1:
            state_machine["Method"] = "getHowToCraftEntity()"
            return getHowToCraftEntity(entity)

        elif text.find("can") != -1:
            state_machine["Method"] = "isPossibleToCraftEntity()"
            return isPossibleToCraftEntity(entity)

        elif text.find("where") != -1:
            state_machine["Method"] = "getWhereToFindEntity()"
            return getWhereToFindEntity(entity)

        elif text.find("what") != -1 or text.find("how") != -1:
            state_machine["Method"] = "getWhatToDoWithEntity()"
            return getWhatToDoWithEntity(entity)

        elif text.find("what") != -1 and ("can") != -1:
            state_machine["Method"] = "getWhatIsPossibleToCraftNow()"
            return getWhatIsPossibleToCraftNow(entity)

        elif text.find("can") != -1 and ("craft") != -1:
            state_machine["Method"] = "isPossibleToCraftEntity()"
            return isPossibleToCraftEntity(entity)

        else:
            state_machine["Method"] = "unknown()"
            return None

    # combat_helper intent #
    if intent == "combat_helper":
        if (text.find("how") != -1 or text.find("can") != -1) and (
                text.find("attack") != -1 or text.find("kill") != -1 or
                text.find("defeat") != -1 and text.find("destroy") != -1):
            state_machine["Method"] = "getLongCombat()"
            return getShortCombat(entity)

        elif text.find("more") != -1 and text.find("about"):
            state_machine["Method"] = "getLongCombat()"
            return getLongCombat(entity)

        elif text.find("what") != -1 and text.find("is") != -1:
            state_machine["Method"] = "getWhatIsEntity()"
            return getWhatIsEntity(entity)

        elif text.find("what") != -1 and text.find("weaknesses") != -1:
            state_machine["Method"] = "getWeaknessesOfEntity()"
            return getWeaknessesOfEntity(entity)

        elif text.find("what") != -1 and (text.find("is") != -1 or text.find("are") != -1):
            state_machine["Method"] = "getWeaknessesOfEntity()"
            return getWeaknessesOfEntity(entity)

        elif text.find("where") != -1 and text.find("find") != -1:
            state_machine["Method"] = "getLocationOfMonster()"
            return getLocationOfMonster(entity)

    state_machine["Method"] = "unknown()"
    return ""


# examples of database queries ##
def getWhoIsEntity(value):
    if value == "Yennefer" or value == "yennefer":
        return GetCharacterInfo("yennefer of vengerberg", "description")
    elif value == "Vesemir":
        return GetCharacterInfo("vesemir", "description")
    elif value == "Ciri":
        return GetCharacterInfo("ciri", "description")
    elif value == "Geralt" or value == "geralt":
        return GetCharacterInfo("geralt of rivia", "description")
    elif value == "Triss":
        return GetCharacterInfo("triss merigold", "description")
    elif value == "Bram":
        return GetCharacterInfo("Bram", "description")
    elif value == "Bastien":
        return GetCharacterInfo("bastien vildenvert", "description")
    elif value == "Elsa":
        return GetCharacterInfo("elsa", "description")
    elif value == "Peter":
        return GetCharacterInfo("peter saar gwynleve", "description")
    elif value == "Dune":
        return GetCharacterInfo("dune vildenvert", "description")
    elif value == "Mislav":
        return GetCharacterInfo("mislav", "description")
    elif value == "Herbalist ":
        return GetCharacterInfo("herbalist (shrine) ", "description")
    elif value == "You" or value == "you":
        return "I am but an humble traveler, always happy to share my stories"
    elif value == "I" or value == "i":
        return "Can't you tell ?"
    elif value is None:
        return "What do you mean by that ?"


def getWhereIsEntity(value):
    if value == "Yennefer":
        return "somewhere, we need to find her"
    elif value == "Vesemir":
        return "in Kaer Morhen, safely waiting for winter to pass"
    elif value == "Ciri":
        return "somewhere, we haven't heard of her for years."
    elif value == "Geralt" or value == "geralt":
        return "right here, are you blind ?"
    else:
        return "somewhere in the continent. I don't know much about it."


# TODO: delete them once the methods are connected with the DB
def getInfoAboutEntity(value):
    return None


def getRelationshipBetweenGeraltAndEntity(value):
    return "Just an humble traveler always happy to share some stories"


def getFactsAboutEntity(value):
    return None


def getHowToCraftEntity(value):
    return GetLocationInfo(value, "ingredients")


def isPossibleToCraftEntity(value):
    return None


def getWhereToFindEntity(value):
    return None


def getWhatToDoWithEntity(value):
    return GetAlchemyInfo(value, "effect")


def getWhatIsPossibleToCraftNow(value):
    return None


def getShortCombat(value):
    return GetEnemyInfo(value, "shortCombatTactic")


def getLongCombat(value):
    return GetEnemyInfo(value, "longCombatTactic")


def getInfoAboutCharacter(value):
    return GetCharacterInfo(value, "description")


def getInfoAboutLocations(value):
    return GetLocationInfo(value, "description")


def getWhatIsEntity(value):
    enemies_list = ["ghoul", "dog", "drowner", "nekker", "wraith", "water hag", "griffin", "Griffin", "noon wraith",
                    "noonwraith",
                    "night wraith", "devil by the well"]

    locations_list = ["White Orchard", "Kaer Morhen", "Novigrad", "Oxenfurt"]

    characters_list = ["Yennefer", "Geralt ", "Triss ", "Ciri", "Vesemir", "Bram",
                       "Bastien",
                       "Elsa", "Dune", "Herbalist", "Merchant", "Mislav",
                       "Peter"]

    if value in locations_list:
        return GetLocationInfo(value, "description")
    elif value in characters_list:
        return GetCharacterInfo(value, "description")
    elif value in enemies_list:
        # Griffin is an unique case, gotta fix the name before starting the db query
        if value == "Griffin" or value == "griffin":
            value = "griffin (creature)"
        return GetEnemyInfo(value, "description")
    elif value == "Witcher":
        return "A witcher is someone who has undergone extensive training, ruthless mental and physical conditioning, " \
               "and mysterious rituals which take place at witcher schools such as Kaer Morhen in preparation for " \
               "becoming an itinerant monsterslayer for hire."
    else:
        return "I have never heard of this before"


def getWhatIsThisEntity(value):  # for game not DB
    return None


def getWeaknessesOfEntity(value):
    return None


def getLocationOfMonster(value):
    return GetEnemyInfo(value, "location")


def initiate_priority_list():
    # 0 : monster 1 : health 2 : quest 3 : zone
    # Gotta add the link to DM at some point.
    priority_level_0 = []
    priority_level_1 = []
    priority_level_2 = []
    priority_level_3 = []
    priority_list = [priority_level_0, priority_level_1, priority_level_2, priority_level_3]
    return priority_list


def get_highest_priority_chat(priority_list):
    for x in priority_list:
        for y in x:
            if y != None:
                return y

    # If there was nothing relevant in the priority list, return "Hmmm"
    return "Hummm"


def remove_from_priority_list(priority_list, element):
    for x in priority_list:
        priority_list[x].remove(element)


def dm():
    try:
        utterance = state_machine["Phrase"]
    except AttributeError:
        utterance = "none"

    try:
        intent = state_machine["Intent"]
    except AttributeError:
        intent = "none"

    try:
        entity = state_machine["Entity"]

    except AttributeError:
        entity = "none"

    # if utterance.find("it") != -1 or utterance.find("her") != -1 or utterance.find("he") != -1 or \
    #         utterance.find("she")!= -1 or utterance.find("him") != -1:
    #     entity = state_machine['P_Entity']
    # else:
    #     entity = state_machine["Entity"]

    if entity is None or entity == "None" or entity == "Narrator":
        if utterance.find("We") != -1 or utterance.find("we") != -1:
            print("we detected bruh")
            info = conversation_get_info(utterance, "we")

        elif utterance.find("they") != -1 or utterance.find("They") != -1 \
                or utterance.find("he") != -1 or utterance.find("He") != -1 \
                or utterance.find("she") != -1 or utterance.find("She") != -1 :
            print("It She He or They detected bruh")
            info = conversation_get_info(utterance, "they")

        elif utterance.find("it") != -1 or utterance.find("It") != -1 \
                or utterance.find("that") != -1 or utterance.find("That") != -1 \
                or utterance.find("this") != -1 or utterance.find("This") != -1 :
            print("It She He or They detected bruh")
            info = conversation_get_info(utterance, "it")

        elif utterance.find("you") != -1 or utterance.find("You") != -1:
            print("You detected bruh")
            info = conversation_get_info(utterance, "you")

    else:

        info = get_info(intent, utterance, entity)

    return info


def conversation_get_info(text, pronoun):
    # Used if there's no entity (use of pronouns) so it'll either be about the character or the previous queries.
    # state_machine["Intent"] = "Conversation"

    try:
        utterance = state_machine["Phrase"]
    except AttributeError:
        utterance = "none"

    try:
        intent = state_machine["Intent"]
    except AttributeError:
        intent = "none"

    try:
        entity = state_machine["Entity"]

    except AttributeError:
        entity = "none"

    try:
        P_utterance = state_machine["P_Phrase"]
    except AttributeError:
        P_utterance = "none"

    try:
        P_intent = state_machine["P_Intent"]
    except AttributeError:
        P_intent = "none"

    try:
        P_entity = state_machine["P_Entity"]

    except AttributeError:
        P_entity = "none"

    if pronoun == "you":
        if text.find("who") != -1:
            state_machine["Method"] = "getWhoIsEntity()"
            return getWhoIsEntity("Geralt")

        elif text.find("what") != -1:
            if text.find("here") != -1:
                state_machine["Intent"] = "Conversation"
                state_machine["Method"] = "Work()"
                return "Work Work"
            else:
                state_machine["Method"] = "getWhatIsEntity()"
                return getWhatIsEntity("Witcher")

        elif text.find("how") != -1:
            state_machine["Intent"] = "Conversation"
            state_machine["Method"] = "Bothersome()"
            return "It's Bothersome, can't you stop doing that ?"

        elif text.find("where") != -1:
            if text.find("from") != -1:
                state_machine["Intent"] = "get_lore"
                return "Rivia"

    elif pronoun == "we":
        if text.find("who") != -1:
            state_machine["Intent"] = "get_lore"
            return "Fellow travelers"

        elif text.find("what") != -1:
            if text.find("here") != -1:
                state_machine["Intent"] = "Conversation"
                state_machine["Method"] = "Work()"
                return "Work Work"
            else:
                state_machine["Method"] = "getWhatIsEntity()"
                return getWhatIsEntity("Witcher")

        elif text.find("how") != -1:
            state_machine["Intent"] = "Conversation"
            state_machine["Method"] = "Bothersome()"
            return "It's Bothersome, can't you stop doing that ?"

        elif text.find("where") != -1:
            state_machine["Intent"] = "Conversation"
            state_machine["Method"] = "CurrentLocation()"
            return "In the middle of nowhere, looking for something that may not even exist. "

    elif pronoun == "it" or pronoun == "they":
        state_machine["Entity"] = state_machine["P_Entity"]
        try:
            entity = state_machine["Entity"]
        except AttributeError:
            entity = "none"

        return get_info(state_machine["Intent"], state_machine["Phrase"], state_machine["Entity"])

    """
    # it the system is not able to get an intent, no info will be retrieved.
    if intent == "none" or entity == "none":
        print("I DID IT")
        state_machine["Method"] = "unknown()"
        return ""

    # get_lore intent #
    if intent == "get_lore":
        if text.find("where") != -1:
            state_machine["Method"] = "getWhereIsEntity()"
            return getWhereIsEntity(entity)
    """
