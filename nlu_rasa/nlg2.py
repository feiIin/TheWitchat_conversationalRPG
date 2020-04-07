import random
#from stateMachine import state_machine
#import stateMachine


# state_machine = {'Intent': "get_lore", 'Entity': "Yennefer", 'Phrase': "Who is Yennefer",  'Info': "the love of my life", 'Method': "getWhoIsEntity()",  'P_Intent': None,
#                  'P_Entity': None, 'P_Phrase': None, 'P_Info': None, 'P_Method': None, }

# entity_list =["Yennefer", "Vesemir", "Geralt", "Ciri", "The Nifgaardian", "The Witcher", "Kaer Morhen", "White Orchard", 
# "Temeria", "Captain Peter", "Vizima", "Elsa", "Bram", "Rhosyn", "Tomira", "Willis", "Tomira%s hut", "mill", "sawmill", "bridge", "crossroads"]

# intent_list = ["greet", "affirm", "deny", "get_lore", "ask_quest_confirmation", "ask_help_quest", "craft_helper", "combat_helper", ]


""" Right now it passes this created state machine to the NLG (see main below). 
    To connect all we should call the actual State Machine"""


state_machine = {'Intent': "combat_helper", 'Entity': "the goat", 'Phrase': "Who is Yennefer",  'Info': "go to the woods and get a knife", 'Method': "getWhoIsEntity()"}

class NLG:

    def __init__(self, dictionary):
        
        """Takes the state_machine as an argument and sets them as its attributes"""
        for key in dictionary:
            setattr(self, key, dictionary[key])
        
        """  Dictionaries with of all possible answers based on the intention of the question """

        self.greet = {
            "key": (f"Hey", f"Hello",f"Mhh, do you need something?")
        }

        self.affirm = {
            "key": (f"Ok, do you want anything else", f"Ok",f"Mhh")
        }

        self.deny = {
            "key": (f"Ok, do you need anything else", f"Ok",f"Mhh")
        }

        self.thanking = {
            "key": (f"Don't worry", f"Ok",f"Mhh")
        }

        """
        self.mood_great = {
            "key": (f" ", f"Ok",f"Mhh")
        }
        """
        self.lore = {
            "key": (f"{self.Entity} is {self.Info}")
        }

        # Right now quest confirmation works the same, not sure how to differentiate them. 
        #       How to connect the action witht this, any idea?
        self.quest = {
            "key": (f"We should {self.Info}", f"I would suggest {self.Info}",f"Let's {self.Info}")
        }

        # The ingredient needs to be the entity her. Maybe we should divide this in two: where to get the ingredient, and how to craft
            # So then the possible answers would be "To craft this you need..." / This can be found in .... /// difficult to make it general
                # altough if we include the type of question (Where/Why/How would be easier and just in one method)
        self.craft = {
            "key": (f"{self.Entity} is {self.Info}")
        }

        # For questions about Where are WE? or were I AM? How to anser?
        self.location = {
            "key": (f"We are at {self.Info}", f"This is {self.Info}", f"This place sounds familiar, I think we are at {self.Info}")
        }

        # Again, generalize questions here or if asks Where to kill, access to the question WHERE.
        self.combat = {
            "key": (f"To kill {self.Entity}, you need to {self.Info}", f"You need to {self.Info}", 
                    f"To defeat {self.Entity} you need to {self.Info}")
        }

        self.inventory = {
            "key": (f"We have various items: {self.Info}", f"This is what you have in the inventory: {self.Info}", f"{self.Info}, that is what you have")
        }

        self.metagame = {
        }

        self.chitchat = {
        }

        self.botchallenge = {

        }

      
    def get_nlg(self):
        if self.Intent == "":
            print("There is no intent")
        if self.Intent == "greet":
            print(self.greet["key"][random.randrange(0,3,1)])
        if self.Intent == "affirm":
            print(self.affirm["key"][random.randrange(0,3,1)])
        if self.Intent == "deny":
            print(self.deny["key"][random.randrange(0,3,1)])
        if self.Intent == "thanking":
            print(self.thanking["key"][random.randrange(0,3,1)])
        if self.Intent == "get_lore" and self.Method =="getWhoIsEntity()":
            #print(f"{self.Entity} is {self.Info}")
            print(self.lore["key"])
        if self.Intent == "ask_quest_confirmation" or self.Intent == "ask_help_quest":
            print(self.quest["key"][random.randrange(0,3,1)])
        if self.Intent == "craft_helper":
            print(self.craft["key"])
        if self.Intent == "location":
            print(self.location["key"][random.randrange(0,3,1)])
        if self.Intent == "combat_helper":
            print(self.combat["key"][random.randrange(0,3,1)])
        if self.Intent == "inventory":
            print(self.thaning["key"][random.randrange(0,3,1)])
        

    def Greet(self):
        if self.Intent == "greet":
            print(self.greet["key"][random.randrange(0,3,1)])
    
    def Affirm(self):
        if self.Intent == "affirm":
            print(self.affirm["key"][random.randrange(0,3,1)])
    
    def Deny(self):
        if self.Intent == "deny":
            print(self.deny["key"][random.randrange(0,3,1)])

    def Thanking(self):
        if self.Intent == "thanking":
            print(self.thanking["key"][random.randrange(0,3,1)])

    def Lore(self):
        if self.Intent == "get_lore" and self.Method =="getWhoIsEntity()":
            #print(f"{self.Entity} is {self.Info}")
            print(self.lore["key"])
    
    def Quest(self):
        if self.Intent == "ask_quest_confirmation" or self.Intent == "ask_help_quest":
            print(self.quest["key"][random.randrange(0,3,1)])
    
    def Craft(self):
        if self.Intent == "craft_helper":
            print(self.craft["key"])
    
    def Location(self):
        if self.Intent == "location":
            print(self.location["key"][random.randrange(0,3,1)])

    def Combat(self):
        if self.Intent == "combat_helper":
            print(self.combat["key"][random.randrange(0,3,1)])
    
    def Inventory(self):
        if self.Intent == "inventory":
            print(self.thaning["key"][random.randrange(0,3,1)])





    
    #when picking up objects: "A journal. Might be useful"
    # When sees blood on the floor:
    #   "A man.. satabbed with a knife, died on the spot. Animals fed on his body, picked his skeleton clean"
    #   "More blood stains over there. But it's not his blood"



if __name__ == "__main__":

    print("==============================================\n")

    nlg = NLG(state_machine)
    nlg.get_nlg()

    print("==============================================\n")



