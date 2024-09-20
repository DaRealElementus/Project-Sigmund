'''Main file, this is the one that is being run'''
import aiFile
import inputOutput
import vosktext

resetString = "debug_reset_EmergencyShower"


#This prgram will not show emotion, instead un-comment the code at the bottom of aiFile.py and run that
while True:
    #Funky input
    userWords = vosktext.Listen()
    print(userWords)
    
    if userWords.lower() == resetString.lower():
        aiFile.history = []
        print("resetting memory")
        inputOutput.SpeakText("resetting memory")
    else:
        output = aiFile.generate_response(userWords)
        try:
            emotion, content = output.split(":")
        except ValueError:
            content = output
            emotion = "happy"
        emotion.strip()

        #Funky output
        print(str(content.strip()))
        inputOutput.SpeakText(str(content.strip()))
