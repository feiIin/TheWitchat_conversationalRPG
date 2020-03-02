from rasa.nlu.model import Interpreter

utterance = "Where is Yennefer?"
model = "./models/nlu_20200302-154348"

# loading the model from one directory or zip file
interpreter = Interpreter.load(model)

# parsing the utterance
interpretation = interpreter.parse(utterance)

# printing the parsed output
print(interpretation)
