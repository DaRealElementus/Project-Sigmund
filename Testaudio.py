# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

#LANI OVER HERE
#https://medium.com/@nimritakoul01/offline-speech-to-text-in-python-f5d6454ecd02

# Function to convert text to
# speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command) 
    engine.runAndWait()
    
    
# Loop infinitely for user to
# speak

# while(1):    
    
#     # Exception handling to handle
#     # exceptions at the runtime
    
#     # use the microphone as source for input.
#     with sr.Microphone() as source2:
        
#         # wait for a second to let the recognizer
#         # adjust the energy threshold based on
#         # the surrounding noise level 
#         r.adjust_for_ambient_noise(source2, duration=0.2)
        
#         #listens for the user's input 
#         audio2 = r.listen(source2)
        
#         # Using google to recognize audio
#         MyText = r.recognize_google(audio2)
#         MyText = MyText.lower()

#         print("Did you say ", MyText)
#         SpeakText(MyText)
