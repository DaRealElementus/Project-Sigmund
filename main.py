'''Main file, this is the one that is being run'''
import aiFile
import inputOutputSystem
import keys
import serial

resetString = "debug_reset_EmergencyShower"

ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM1'

while True:
    #Funky input
    userWords = input("\n")
    #^ replace with actual input func
    if userWords == resetString:
        aiFile.history = []
    else:
        output = aiFile.generate_response(userWords)
        emotion, content = output.split(":")
        emotion.strip()
        # if emotion in aiFile.emotions:
        #     emotion = str.encode(emotion)
        #     ser.write(emotion)
        
        #Funky output
        print(str(content.strip()))
        #^replace with actual output func