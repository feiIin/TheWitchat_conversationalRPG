import random
from stateMachine import state_machine

class NLG:


    def __init__(self, dictionary):
        """Takes the state_machine as an argument and sets them as its attributes"""
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def lore(self):
        if self.Intent == "get_lore" and self.Entity == "Yennefer" and self.Method == "getWhoIsEntity()":
            print(f"{self.Entity} is {self.Info}")
            # return f"{self.Entity} is {self.Info}"
        if self.Intent == "get_lore" and self.Entity == "Vesemir" and self.Method == "getWhoIsEntity()":
            print(f"{self.Entity} is {self.Info}")
            # return f"{self.Entity} is {self.Info}"


    def greet(self):
        if self.Intent == "greet":
            print('Hello')


def nlg():
    print("==============================================\n")

    nlg = NLG(state_machine)
    nlg.lore()
    nlg.greet()

    print("==============================================\n")
    # return phrase