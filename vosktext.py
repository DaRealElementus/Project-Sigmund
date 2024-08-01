import vosk
import pyaudio
import json

# Here I have downloaded this model to my PC, extracted the files 
# and saved it in local directory
# Set the model path

# Initialize the model with model-path
model = vosk.Model(lang="en-us")

rec = vosk.KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8192)

print("Listening for speech. Say 'Terminate' to stop.")
# Start streaming and recognize speech
while True:
    data = stream.read(4096)#read in chunks of 4096 bytes
    if rec.AcceptWaveform(data):#accept waveform of input voice
        # Parse the JSON result and get the recognized text
        result = json.loads(rec.Result())
        recognized_text = result['text']
        print(recognized_text)
        
        # Check for the termination keyword
        if "terminate" in recognized_text.lower():
            print("Termination keyword detected. Stopping...")
            break

# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate the PyAudio object
p.terminate()

