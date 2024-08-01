'''File to utilise the Microphone speaker system'''
import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
    

def recogniseAudio():
    with sr.Microphone() as source2:
    
   
        r.adjust_for_ambient_noise(source2, duration=0.2)
    
        audio2 = r.listen(source2, timeout=5)
        
        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()
        print(MyText)
        return MyText
        
