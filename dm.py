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

'''
from nlu import get_intent
from stateMachine import state_machine

# RULES ##############################


def get_info(intent, text, entity):
    # get_lore intent #
    if intent == "get_lore":
        if text.find("where") != -1:
            # query db asking for the location of the entities + return it to nlg
            return getWhereIsEntity(entity)
        elif text.find("who") != -1:
            state_machine["Method"] = "getWhoIsEntity()"
            return getWhoIsEntity(entity)
        elif text.find("you") != -1 or text.find("between") != -1:
            return getRelationshipBetweenGeraltAndEntity(entity)
        elif text.find("more") != -1 or text.find("tell") != -1:
            return getFactsAboutEntity(entity)
        else:
            return None

    # craft_helper intent #
    if intent == "craft_helper":
        if text.find("how") != -1 and text.find("can") != -1 or text.find("how") != -1 and text.find("do") != -1:
            return getHowToCraftEntity(entity)
        elif text.find("can") != -1:
            return isPossibleToCraftEntity(entity)
        elif text.find("where") != -1:
            return getWhereToFindEntity(entity)
        elif text.find("what") != -1 or text.find("how") != -1 :
            return getWhatToDoWithEntity(entity)
        elif text.find("what") != -1 and ("can") != -1:
            return getWhatIsPossibleToCraftNow(entity)
        elif text.find("can") != -1 and ("craft") != -1:
            return isPossibleToCraftEntity(entity)
        else:
            return None

    # combat_helper intent #
    hasSaid = False
    if intent == "combat_helper":
        if hasSaid == False:
            if text.find("how") != -1 and text.find("attack") != -1 or text.find("kill") != -1 or text.find("defeat") != -1 or text.find("how") != -1 and text.find("destroy") != -1:
                hasSaid = True
                return getShortCombat(entity)
        else:
            return getLongCombat(entity)
    elif text.find("what") != -1 and text.find("is") != -1:
        return getWhatIsEntity(entity)
    elif text.find("what") != -1 and text.find("weaknesses") != -1:
        return getWeaknessesOfEntity(entity)
    elif text.find("where") != -1 and text.find("is") != -1:
        return getLocationOfMonster(entity)

# examples of database queries ##


def getWhoIsEntity(value):
    if value == "Yennefer":
        return "the love of my life"
    elif value == "Vesemir":
        return "the oldest and most experienced witcher"
    elif value == "Ciri":
        return "princess of Cintra"


def getWhereIsEntity(value):
    if value == "Yennefer":
        return "somewhere, we need to find her"
    elif value == "Vesemir":
        return "Kaer Morhen"
    elif value == "Ciri":
        return "somewhere"


def getInfoAboutEntity(value):
    return None


def getRelationshipBetweenGeraltAndEntity(value):
    return None


def getFactsAboutEntity(value):
    return None


def getHowToCraftEntity(value):
    return None


def isPossibleToCraftEntity(value):
    return None


def getWhereToFindEntity(value):
    return None


def getWhatToDoWithEntity(value):
    return None


def getWhatIsPossibleToCraftNow(value):
    return None


def getShortCombat(value):
    return None


def getLongCombat(value):
    return None


def getWhatIsEntity(value):
    return None


def getWhatIsThisEntity(value): # for game not DB
    return None


def getWeaknessesOfEntity(value):
    return None


def getLocationOfMonster(value):
    return None


def dm():
    utterance = state_machine["Phrase"].lower()
    entity = state_machine["Entity"]
    intent = state_machine["Intent"]
    if utterance.find("it") != -1 or utterance.find("her") != -1 or utterance.find("he") != -1 or \
            utterance.find("she")!= -1 or utterance.find("him") != -1:
        entity = state_machine['P_Entity']
    info = get_info(intent, utterance, entity)
    return info

#
# def main():
#     utterance = "Who is Yennefer"
#     result = get_intent(utterance)
#     # print(result)
#     intent = result["intent"]["name"]
#     entities_names = [x["value"] for x in result["entities"]]
#     text = result["text"].lower()
#     print(intent)main
#     print(entities_names[0])
#
#     previous_machine = {'Intent': None, 'Entity': None, 'Phrase': None, 'Info': None}
#
#     if text.find("it") != -1 or text.find("her") != -1 or text.find("he") != -1 or text.find("she") != -1 or text.find("him") != -1:
#         entities_names[0] = previous_machine['Entity']
#
#     info = get_info(intent, text, entities_names[0])
#
#     previous_machine['Intent'] = intent
#     previous_machine['Entity'] = entities_names[0]
#     previous_machine['Phrase'] = text
#     previous_machine['Info'] = info
#
#     print(info)


# if __name__ == "__main__":
#     main()