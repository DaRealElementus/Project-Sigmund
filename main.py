'''Main file, this is the one that is being run'''
import aiFile
import serial
import inputOutput
import vosktext
def play_movie(path):
        from os import startfile
        startfile(path)

resetString = "debug_reset_EmergencyShower"
singString = "me a song"

ser = serial.Serial()
ser.baudrate = 19200                                     
ser.port = 'COM1'

#This prgram will not show emotion, instead un-comment the code at the bottom of aiFile.py and run that
while True:
    #Funky input
    userWords = vosktext.Listen()
    print(userWords)
    
    #^ replace with actual input func
    if userWords.lower() == resetString.lower():
        aiFile.history = []
        print("resetting memory")
        inputOutput.SpeakText("resetting memory")
    if userWords.lower().__contains__(singString.lower()):
        play_movie("Perfectly Fine.mp4")

    else:
        output = aiFile.generate_response(userWords)
        emotion, content = output.split(":")
        # emotion.strip()
        # if emotion in aiFile.emotions:
        #     emotion = str.encode(emotion)
        #     ser.write(emotion)
        
        #Funky output
        print(str(content.strip()))
        inputOutput.SpeakText(str(content.strip()))
        #^replace with actual output func