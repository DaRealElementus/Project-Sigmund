'''Main file, this is the one that is being run'''
import aiFile
import motorytest
import inputOutput
import vosktext
import threading
import asyncio

resetString = "debug_reset_EmergencyShower"
#motory.setup()
#thread = threading.Thread(target=motorytest)
#thread.start()

#This prgram will not show emotion, instead un-comment the code at the bottom of aiFile.py and run that
async def main():
    while True:
        await motorytest.loop()
        #Funky input
        userWords = vosktext.Listen()
        print(userWords)
        
        #^ replace with actual input func
        if userWords.lower() == resetString.lower():
            aiFile.history = []
            print("resetting memory")
            inputOutput.SpeakText("resetting memory")
        else:
            output = aiFile.generate_response(userWords)
            emotion, content = output.split(":")
            emotion.strip()
            if emotion in aiFile.emotions:
                motorytest.emotion = emotion
            
            #Funky output
            print(str(content.strip()))
            inputOutput.SpeakText(str(content.strip()))
            #^replace with actual output func

if __name__ == '__main__':
    asyncio.run(main())  # Start the asyncio event loop