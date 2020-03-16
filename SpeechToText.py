import speech_recognition as sr

# This function checks for microphone input and sents this to google Speech to text to parse
# it then returns a transcript of what it thinks you've said as a string
def RecordVoice():
    recording = True
    r = sr.Recognizer()
    transcript = ""

    # Makes the microphone record sound
    with sr.Microphone() as source:

        # Adjusts the microphone levels, sound levels and phrase time limit
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 700
        print("Please say something to Geralt")
        audio = r.listen(source, timeout= 2, phrase_time_limit= 5)

        try:
            print("You have said the following: \n" +r.recognize_google(audio))
            transcript = str(r.recognize_google(audio))
            recording = False
        except Exception as e:
            recording = False
            transcript = "no valid sound"
            print("Error : " + str(e))

    return transcript

# print(pyaudio.pa.__file__)