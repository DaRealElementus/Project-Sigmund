import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
i=0
for voice in voices:
    if "engl" in voice.id:
        print(voice, voice.id, i)
        engine.setProperty('voice', voice.id)
        engine.say("Hello World!")
        engine.runAndWait()
        engine.stop()
    i += 1