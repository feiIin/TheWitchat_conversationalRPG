import speech_recognition as sr
import keyboard



def main():
    recording = True
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 700
        print("Please say something to Geralt")
        audio = r.listen(source, timeout= 2, phrase_time_limit= 5)

        try:
            print("You have said the following: \n" +r.recognize_google(audio))
            recording = False
        except Exception as e:
            recording = False
            print("Error : " + str(e))


recording = False
while True:
    try:
        if keyboard.is_pressed('q') and not recording:  # if key 'q' is pressed
            main()
            break
    except:
        break

# if __name__ == "__main__":
#     main()