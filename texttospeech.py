import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170 )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Starting the system...")
speak("Starting the system...")
print("Initializing packages...")
speak("Initializing packages...")
print("Importing libraries...")
speak("Importing libraries...")
print("JARVIS..")
speak("JARVIS..")
print("Your personal A.I. assistant is ready...") 
speak("Your personal A.I. assistant is ready...") 