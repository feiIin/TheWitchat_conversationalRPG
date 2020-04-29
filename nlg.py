import random

# from stateMachine import state_machine
# import stateMachine


# state_machine = {'Intent': "get_lore", 'Entity': "Yennefer", 'Phrase': "Who is Yennefer",  'Info': "the love of my life", 'Method': "getWhoIsEntity()",  'P_Intent': None,
#                  'P_Entity': None, 'P_Phrase': None, 'P_Info': None, 'P_Method': None, }

# entity_list =["Yennefer", "Vesemir", "Geralt", "Ciri", "The Nifgaardian", "The Witcher", "Kaer Morhen", "White Orchard", 
# "Temeria", "Captain Peter", "Vizima", "Elsa", "Bram", "Rhosyn", "Tomira", "Willis", "Tomira%s hut", "mill", "sawmill", "bridge", "crossroads"]

# intent_list = ["greet", "affirm", "deny", "get_lore", "ask_quest_confirmation", "ask_help_quest", "craft_helper", "combat_helper", ]


""" Right now it passes this created state machine to the NLG (see main below). 
    To connect all we should call the actual State Machine"""
"""
state_machine = {'Intent': "combat_helper", 'Entity': "the goat", 'Phrase': "Who is Yennefer",
                  'Info': "go to the woods and get a knife", 'Method': "getWhatIsEntity()"}
"""


class NLG:

    def __init__(self, dictionary):

        """Takes the state_machine as an argument and sets them as its attributes"""
        for key in dictionary:
            setattr(self, key, dictionary[key])

        """  Dictionaries with of all possible answers based on the intention of the question """

        self.greet = {
            "key": (f"Hey", f"Hello", f"Hummm, do you need something?")
        }

        self.affirm = {
            "key": (f"Ok, do you want anything else", f"Ok", f"Hummm")
        }

        self.deny = {
            "key": (f"Ok, do you need anything else", f"Ok", f"Hummm")
        }

        self.thanking = {
            "key": (f"Don't worry", f"Ok", f"You're welcome")
        }

        """
        self.mood_great = {
            "key": (f" ", f"Ok",f"Hummm")
        } 
        """

        self.loreWhere = {
            "key": (f"{self.Entity} is {self.Info}", f"You can find {self.Entity}  {self.Info}")
        }

        self.lore = {
            "key": (f"{self.Info}")
        }
        self.loreFacts = {
            "key": f"I can tell you that {self.Info}"
        }

        self.loreDescription = f"{self.Info}"

        # Right now quest confirmation works the same, not sure how to differentiate them. 
        #       How to connect the action witht this, any idea?
        self.quest = {
            "key": (f"We should {self.Info}", f"I would suggest {self.Info}", f"Let's {self.Info}")
        }

        # The ingredient needs to be the entity her. Maybe we should divide this in two: where to get the ingredient, and how to craft
        # So then the possible answers would be "To craft this you need..." / This can be found in .... /// difficult to make it general
        # altough if we include the type of question (Where/Why/How would be easier and just in one method)
        self.craftWith = {
            "key": (f"With {self.Entity} you can craft {self.Info}")
        }
        self.craftHow = {
            "key": (f"To craft {self.Entity} you have to {self.Info}")
        }
        self.craftWhere = {
            "key": (
            f"You can find {self.Entity} in {self.Info}", f"You can find it in {self.Info}", f"Go to {self.Info}")
        }
        self.craftNow = {
            "key": (f"{self.Entity} is {self.Info}")
        }
        self.craftCheck = {
            "key": (f"You need {self.Info} to craft {self.Entity}")
        }

        # For questions about Where are WE? or were I AM? How to anser?
        self.location = f"{self.Info}"

        # Again, generalize questions here or if asks Where to kill, access to the question WHERE.
        self.combatWhat = f"It is a monster. {self.Info}"

        """  Old one, Doesn't work with every query
        self.combatWhere = {
            "key": (f"To kill {self.Entity}, you need to go to {self.Info}", f"{self.Entity} is in {self.Info}",
                    f"To defeat {self.Entity} you need to go to {self.Info}")
        }
        """

        self.combatWhere = f"{self.Info}"

        self.combatHow = {
            "key": (f"To kill {self.Entity}, you need to {self.Info}", f"You need to {self.Info}",
                    f"To defeat {self.Entity} you need to {self.Info}")
        }

        self.combatTactic = f"{self.Info}"

        self.combatWeak = {
            "key": (f"The weakness of {self.Entity} are {self.Info}")
        }

        self.inventory = {
            "key": (f"We have various items: {self.Info}", f"This is what you have in the inventory: {self.Info}",
                    f"{self.Info}, that is what you have")
        }

        self.metagame = {
        }

        self.chitchat = {
            "key": (f"War... War never changes",
                    f"You know the rules, never work for free",
                    f"Folks Don't Expect Witchers To Save Them From Themselves.",
                    f"Evil Is Evil. Lesser, Greater, Middling, Makes No Difference. "
                    f"The Degree Is Arbitrary, The Definitions Blurred.",
                    f"There's a grain of truth in every fairy tale.",
                    f"When you know about something it stops being a nightmare. When you know how to fight something, "
                    f"it stops being so threatening.",
                    f"Friendship is magic, and magic is heresy",
                    f"Do you know when stories stop being stories? The moment someone begins to believe in them.",
                    f"Every myth, every fable must have some roots. Something lies among those roots.",
                    f"I could never resist the temptation of having a look at something that doesn't exist.",
                    f"No king rules forever",
                    f"People like to invent monsters and monstrosities. Then they seem less monstrous themselves. ",
                    f"Time eats away at memories, distorts them. Sometimes we only remember the good... "
                    f"sometimes only the bad.",
                    f"Why men throw their lives away attacking an armed witcher... I'll never know. "
                    f"Something wrong with my face?",
                    f"The right man in the wrong place can make all the difference in the world.",
                    f"War is where the young and stupid are tricked by the old and bitter into killing each other",
                    f"Hope is what makes us strong. It is why we are here. "
                    f"It is what we fight with when all else is lost.",
                    f"Men are but flesh and blood. They know their doom, but not the hour.",
                    f"Dreams have a nasty habit of going bad when you’re not looking.",
                    f"Stand in the ashes of a million dead souls and ask the ghosts if honor matters. "
                    f"Their silence is your answer.",
                    f"The cake is a lie",
                    f"Kept you waiting, huh?"
                    )
        }

        self.conversation = f"{self.Info}"

        self.Bothersome = {
            "key": (f"You're noisy...", f"don't you have anything better to do ?",
                    f"Adventures used to be much more relaxing before you joined me.",
                    f"Enough questions, focus on the road ahead",
                    f"It's getting quite bothersome, can't you stop doing that ?")
        }

        self.Work = {
            "key": (f"A contract, as usual",
                    f"What is expected from a Witcher, Slay monsters",
                    f"Cleansing these lands, one step at a time",
                    f"Got work to do",
                    f"Same old story, Witchers killing monsters.")
        }

        self.CurrentLocation = {
            "key": (f"In the middle of nowhere, looking for something that may not even exist",
                    f"Lost.",
                    f"Somewhere... Over the rainbow",
                    f"In Nilfgaard  ")
        }

        self.botchallenge = {

        }

    def Greet(self):
        if self.Intent == "greet":
            return self.greet["key"][random.randrange(0, 3, 1)]

    def Affirm(self):
        if self.Intent == "affirm":
            return self.affirm["key"][random.randrange(0, 3, 1)]

    def Deny(self):
        if self.Intent == "deny":
            return self.deny["key"][random.randrange(0, 3, 1)]

    def Thanking(self):
        if self.Intent == "thanking":
            return self.thanking["key"][random.randrange(0, 3, 1)]

    def Lore(self):
        if self.Intent == "get_lore" and self.Method == "getWhoIsEntity()" or self.Method == "getInfoAboutEntity()" or self.Method == "getRelationshipBetweenGeraltAndEntity()":
            # print(f"{self.Entity} is {self.Info}")
            return self.lore["key"]
        if self.Intent == "get_lore" and self.Method == "getWhereIsEntity()":
            # print(f"{self.Entity} is {self.Info}")
            return self.loreWhere["key"][random.randrange(0, 2, 1)]
        if self.Intent == "get_lore" and self.Method == "getFactsAboutEntity()":
            # print(f"{self.Entity} is {self.Info}")
            return self.loreFacts["key"]
        if self.Intent == "get_lore" and self.Method == "getWhatIsEntity()":
            return self.loreDescription
        else :
            return self.loreDescription

    def Craft(self):
        if self.Intent == "craft_helper" and self.Method == "getHowToCraftEntity()":
            return self.craftHow["key"]
        if self.Intent == "craft_helper" and self.Method == "getWhereToFindEntity()":
            return self.craftWhere["key"][random.randrange(0, 3, 1)]
        if self.Intent == "craft_helper" and self.Method == "getWhatToDoWithEntity()":
            return self.craftWith["key"]
        if self.Intent == "craft_helper" and self.Method == "getWhatIsPossibleToCraftNow()":
            return self.craftNow["key"]
        if self.Intent == "craft_helper" and self.Method == "isPossibleToCraftEntity()":
            return self.craftCheck["key"]

    def Combat(self):
        # getShortCombat getLongCombat
        if self.Intent == "combat_helper" and self.Method == "getShortCombat()" or self.Method == "getLongCombat()":
            return self.combatTactic
        if self.Intent == "combat_helper" and self.Method == "getWhatIsEntity()" or self.Method == "getWhatIsThisEntity()":
            return self.combatWhat
        if self.Intent == "combat_helper" and self.Method == "getWeaknessesOfEntity()":
            return self.combatWeak["key"]
        if self.Intent == "combat_helper" and self.Method == "getLocationOfMonster()":  # monster is in entity
            # return self.combatWhere["key"][random.randrange(0, 3, 1)]
            if self.Entity is not None and self.Info is not None:
                if (self.Info.find(self.Entity) != -1) or self.Info.find("griffin") != -1:
                    self.combatWhere = f"{self.Entity} can usually be found near {self.Info}"
            return self.combatWhere
        if self.Intent == "combat_helper" and self.Method == "getHowKillfMonster()":  # monster is in entity
            return self.combatHow["key"][random.randrange(0, 3, 1)]

    def Quest(self):
        if self.Intent == "ask_quest_confirmation" or self.Intent == "ask_help_quest":
            return self.quest["key"][random.randrange(0, 3, 1)]

    def Location(self):
        if self.Intent == "location":
            if self.Method == "getWhereIsEntity()":
                return self.location
            else :
                return self.CurrentLocation["key"][random.randrange(0, 4, 1)]

    def Inventory(self):
        if self.Intent == "inventory":
            return self.thaning["key"][random.randrange(0, 3, 1)]

    def ChitChat(self):
        return self.chitchat["key"][random.randrange(0, 22, 1)]

    def Conversation(self):
        if self.Method == "Bothersome()":
            return self.Bothersome["key"][random.randrange(0, 5, 1)]
        elif self.Method == "Work()":
            return self.Work["key"][random.randrange(0, 5, 1)]
        elif self.Method == "CurrentLocation()":
            return self.CurrentLocation["key"][random.randrange(0, 4, 1)]
        else:
            return self.conversation

    def get_nlg(self):
        if self.Intent == "":
            print("There is no intent")
        if self.Intent == "greet":
            return NLG.Greet(self)
        if self.Intent == "affirm":
            return NLG.Affirm(self)
        if self.Intent == "deny":
            return NLG.Deny(self)
        if self.Intent == "thanking":
            return NLG.Thanking(self)
        if self.Intent == "get_lore":
            return NLG.Lore(self)
        if self.Intent == "ask_quest_confirmation" or self.Intent == "ask_help_quest":
            return NLG.Quest(self)
        if self.Intent == "craft_helper":
            return NLG.Craft(self)
        if self.Intent == "location":
            return NLG.Location(self)
        if self.Intent == "combat_helper":
            return NLG.Combat(self)
        if self.Intent == "inventory":
            return NLG.Inventory(self)
        if self.Intent == "Conversation":
            return NLG.Conversation(self)

    # state_machine = {'Intent': "", 'Entity': "", 'Phrase': "",  'Info': "", 'Method': "",
    #                  'P_Intent': None, 'P_Entity': None, 'P_Phrase': None, 'P_Info': None, 'P_Method': None, }

    # when picking up objects: "A journal. Might be useful"
    # When sees blood on the floor:
    #   "A man.. satabbed with a knife, died on the spot. Animals fed on his body, picked his skeleton clean"
    #   "More blood stains over there. But it's not his blood"


"""
if __name__ == "__main__":
    print("==============================================\n")
#
    nlg = NLG(state_machine)
    nlg.get_nlg()
#
    print("==============================================\n")

"""
