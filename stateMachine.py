# State machine as memory of the bot
# The state machine is a python dictionary which stores the information about current and past phrase.
# The sate machine should be common to all the bot, and updated using the set methods.
# The "current states" should be passed as "previous states" after the  bot selects the nlg template to use


state_machine = {'Intent': None, 'Entity': None, 'Phrase': None,  'Info': None, 'Method': None,  'P_Intent': None,
                 'P_Entity': None, 'P_Phrase': None, 'P_Info': None, 'P_Method': None, }

# Example of state during interaction:
# Dict = {'Intent': 'getLore', 'Entity' : 'Yennifer', 'Phrase': 'Who is yennifer', 'Info': 'the love of my life',
#           'Method':'getWhoIsEntity()'}

##### set the info in the state machine ########

def set_intent(intent):
    state_machine['Intent'] = intent


def set_entity(entity):
    state_machine['Entity'] = entity


def set_phrase(phrase):
    state_machine['Phrase'] = phrase


def set_info(info):
    state_machine['Info'] = info


def set_p_intent(intent):
    state_machine['Intent'] = intent


def set_p_entity(entity):
    state_machine['Entity'] = entity


def set_p_phrase(phrase):
    state_machine['Phrase'] = phrase


def set_p_info(info):
    state_machine['Info'] = info


def set_p_method(method):
    state_machine['P_Method'] = method

def set_method(method):
    state_machine['Method'] = method


##### set the info in the state machine ########


def get_intent():
    return state_machine['Intent']


def get_entity():
    return state_machine['Entity']


def get_phrase():
    return state_machine['Phrase']


def get_info():
    return state_machine['Info']


def get_p_intent():
    return state_machine['Intent']


def get_p_entity():
    return state_machine['Entity']


def get_p_phrase():
    return state_machine['Phrase']


def get_p_info():
    return state_machine['Info']


def get_p_method():
    return state_machine['P_Method']


def get_method():
    return state_machine['Method']

#### to test #####
#
# def main():
#     set_entity("Yennefer")
#     set_intent("get_lore")
#     set_method("getWhoIsEntity(value)")
#     print(get_entity())
#     print(get_intent())
#     print(get_method())
#     print(state_machine)
#
#
#
# if __name__ == "__main__":
#     main()
