from rasa.nlu.model import Interpreter

def get_intent(utterance):
    model = "nlu_rasa/models/nlu"

    interpreter = Interpreter.load(model)
    interpretation = interpreter.parse(utterance)

    return interpretation
