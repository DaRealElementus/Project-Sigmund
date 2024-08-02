import vosk
import pyaudio
import json
import keyboard

# Here I have downloaded this model to my PC, extracted the files 
# and saved it in local directory
# Set the model path

# Initialize the model with model-path
model = vosk.Model(lang="en-us")

rec = vosk.KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()


# Start streaming and recognize speech
def Listen():
        full_text = ''
        while not keyboard.is_pressed(' '):
            pass
        stream = p.open(format=pyaudio.paInt16,
        channels=2,
        rate=48000,
        input=True,
        frames_per_buffer=2048,
        input_device_index=1)
        print("Listening started")
        while True:
            data = stream.read(4096, False)#read in chunks of 4096 bytes
            if rec.AcceptWaveform(data):#accept waveform of input voice
                # Parse the JSON result and get the recognized text
                result = json.loads(rec.Result())
                recognized_text = result['text']
                full_text += recognized_text
                
            if not keyboard.is_pressed(' '):
                break
        print("listening stopped")
        stream.stop_stream()
        stream.close()
        return full_text