from rasa.nlu.model import Interpreter

def get_intent(utterance):
    model = "nlu_rasa/models/nlu_20200302-154348"

    interpreter = Interpreter.load(model)
    interpretation = interpreter.parse(utterance)

    return interpretation
