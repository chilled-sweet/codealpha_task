                                                                # Voice Aassistant

import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the Speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak a given message
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():

        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try :
            text = r.recognize_google(audio)
            print(f"\nYou Said : {text}\n")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said !")
        except sr.RequestError:
            print("Sorry, my speech recognition service is currently down !")


# Define a function to Get user name
# def get_user_name():
#     user_name = listen()
#     speak(f"Hi {user_name} ! What can I do for you today !")

# Define a funnction to get a current time
def get_time():
    now = datetime.datetime.now()
    hour = now.strftime('%I')
    minute = now.strftime('%M')
    am_pm = now.strftime("%p")
    speak(f"The time is {hour}:{minute} {am_pm}.")

# Define a function to get the assistant's name
def get_assi_name():
    speak("My name is Python Voice Assistent")

# Define a function to create a new note
def create_note():
    speak("What should I write in Note ?")
    note_text = listen()
    filename =datetime.datetime.now().strftime("%Y+%m+%d_%M+%M+%S") + ".txt"
    with open(filename,'w') as f:
        f.write(note_text)
    speak("Note Has Been saved !")


# Define a main function to run the voice assistant
if __name__ == "__main__":
    # Greet the user
    speak("Welcome! I'm your voice assistant.")
    # speak("Before Moving forward Sir, can i know your name ?")

    #Listen for useer input
    while True:
        command = listen()
        # get_user_name()
        # if listen() in command:
        #     get_user_name()
        if "hello" in command:
            speak("Hi there ")
        elif "how r u"in command:
            speak("I am doing well, Thank you ")
        elif "what is your name" in command :
            get_assi_name()
        elif 'what was current time' in command:
            get_time()
        elif "create a note" in command:
            create_note()
        elif "good bye" in command:
            speak("Good Bye !")
            break
        else:
            speak("I'm Sorry, didn't understand what you said.")