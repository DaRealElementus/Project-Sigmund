'''File to utilise the Microphone speaker system'''
import pyttsx3 


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty('voice', "english-us")
    engine.say(command) 
    engine.runAndWait()
    

