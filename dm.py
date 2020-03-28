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


'''
from nlu import get_intent
from stateMachine import state_machine
from MongodbScript import GetEnemyInfo, GetAlchemyInfo, GetCharacterInfo, GetLocationInfo

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
            state_machine["Method"] = "getRelationshipBetweenGeraltAndEntity()"
            return getRelationshipBetweenGeraltAndEntity(entity)
        elif text.find("more") != -1 or text.find("tell") != -1:
            state_machine["Method"] = "getFactsAboutEntity()"
            return getFactsAboutEntity(entity)
        else:
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
            return None

    # combat_helper intent #
    hasSaid = False
    if intent == "combat_helper":
        if hasSaid == False:
            if text.find("how") != -1 and text.find("attack") != -1 or text.find("kill") != -1 or text.find("defeat") != -1 or text.find("how") != -1 and text.find("destroy") != -1:
                hasSaid = True
                state_machine["Method"] = "getShortCombat()"
                return getShortCombat(entity)
        else:
            return getLongCombat(entity)
    elif text.find("what") != -1 and text.find("is") != -1:
        state_machine["Method"] = "getWhatIsEntity()"
        return getWhatIsEntity(entity)
    elif text.find("what") != -1 and text.find("weaknesses") != -1:
        state_machine["Method"] = "getWeaknessesOfEntity()"
        return getWeaknessesOfEntity(entity)
    elif text.find("where") != -1 and text.find("is") != -1:
        state_machine["Method"] = "getLocationOfMonster()"
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


def getWhatIsEntity(value):
    return None


def getWhatIsThisEntity(value): # for game not DB
    return None


def getWeaknessesOfEntity(value):
    return None


def getLocationOfMonster(value):
    return GetEnemyInfo(value, "location")


def dm():
    utterance = state_machine["Phrase"].lower()
    entity = state_machine["Entity"]
    intent = state_machine["Intent"]
    if utterance.find("it") != -1 or utterance.find("her") != -1 or utterance.find("he") != -1 or \
            utterance.find("she")!= -1 or utterance.find("him") != -1:
        entity = state_machine['P_Entity']
    info = get_info(intent, utterance, entity)
    return info
