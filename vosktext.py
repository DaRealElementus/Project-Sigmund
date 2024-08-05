import vosk
import pyaudio
import json
import keyboard

# Here I have downloaded this model to my PC, extracted the files 
# and saved it in local directory
# Set the model path

# Initialize the model with model-path
model = vosk.Model(lang="en-us")

rec = vosk.KaldiRecognizer(model, 48000)
p = pyaudio.PyAudio()        

# Start streaming and recognize speech
def Listen():                                              
    full_text = ''
    while not keyboard.is_pressed(' '):
        pass
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=48000, input=True, frames_per_buffer=2048)
    try:
        while True:
            data = stream.read(2048, False)  # read in chunks of 2048 bytes
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
            else:
                res = json.loads(rec.PartialResult())
            if not keyboard.is_pressed(' '):
                break
    finally:
        stream.stop_stream()
        stream.close()
        return json.loads(rec.FinalResult())['text']

# while True:
#      funi = Listen()
#      print(funi)