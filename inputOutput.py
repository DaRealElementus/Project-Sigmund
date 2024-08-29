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

#'''File to utilise the Microphone speaker system'''
#import pyttsx3 
#import pygame
#from pygame import mixer as mix
#import os

#os.environ['SDL_AUDIODRIVER'] = 'pulse'
#pygame.init()
#mix = pygame.mixer
#mix.init()
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[12].id)
#engine.setProperty('rate', 155)


# Function to convert text to
# speech
#def SpeakText(command):
#    # Initialize the engine
#    engine.save_to_file(command, "Words.wav") 
#    engine.runAndWait()
#    if os.path.exists("Words.wav"):
#        mix.music.load("Words.wav")
#        mix.music.play()
#        while pygame.mixer.music.get_busy() == True:
#            continue
#        mix.music.unload()
#        os.remove("Words.wav")
#   else:
#       print("The file does not exist")

#SpeakText("hello")