'''File to utilise the Microphone speaker system'''
import pyttsx3 


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[12].id)
engine.setProperty('rate', 155)
    

# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine.say(command) 
    engine.runAndWait()
