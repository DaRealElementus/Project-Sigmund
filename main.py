'''Main file, this is the one that is being run'''
import aiFile
import inputOutputSystem
import keys
import serial
import Testaudio

resetString = "debug_reset_EmergencyShower"

ser = serial.Serial()
ser.baudrate = 19200                                     
ser.port = 'COM1'

#This prgram will not show emotion, instead un-comment the code at the bottom of aiFile.py and run that

while True:
    #Funky input
    userWords = input("\n")
    #^ replace with actual input func
    if userWords.lower() == resetString.lower():
        aiFile.history = []
        print("resetting memory")
        Testaudio.SpeakText("resetting memory")
    else:
        output = aiFile.generate_response(userWords)
        emotion, content = output.split(":")
        emotion.strip()
        # if emotion in aiFile.emotions:
        #     emotion = str.encode(emotion)
        #     ser.write(emotion)
        
        #Funky output
        print(str(content.strip()))
        Testaudio.SpeakText(str(content.strip()))
        #^replace with actual output func