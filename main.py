'''Main file, this is the one that is being run'''
import aiFile
import motorytest
import inputOutput
import vosktext
import asyncio
import os

resetString = "debug_reset_EmergencyShower"
SongString = "Me a Song"
def play_movie(path):
        os.startfile(path)

#motory.setup()
#thread = threading.Thread(target=motorytest)
#thread.start()

#This prgram will not show emotion, instead un-comment the code at the bottom of aiFile.py and run that
def main():
    while True:
        #Funky input
        userWords = vosktext.Listen()
        print(userWords)
        
        #^ replace with actual input func
        if userWords.lower() == resetString.lower():
            aiFile.history = []
            print("resetting memory")
            inputOutput.SpeakText("resetting memory")
        elif userWords.lower() == SongString.lower():
            play_movie("Perfectly Fine.mp4")
        else:
            output = aiFile.generate_response(userWords)
            try:
                emotion, content = output.split(":")
            except ValueError:
                content = output
                emotion = "happy"
            emotion.strip()
            if emotion in aiFile.emotions:
                motorytest.emotion = emotion
            
            #Funky output
            print(str(content.strip()))
            inputOutput.SpeakText(str(content.strip()))
            #^replace with actual output func

if __name__ == '__main__':
    asyncio.run(motorytest.loop())  # Start the asyncio event loop
    main()