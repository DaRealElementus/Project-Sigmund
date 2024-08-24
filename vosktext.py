import vosk
import pyaudio
import json
import keyboard
import numpy as np

# Here I have downloaded this model to my PC, extracted the files 
# and saved it in local directory
# Set the model path

# Initialize the model with model-path
model = vosk.Model(lang="en-us")

rec = vosk.KaldiRecognizer(model, 48000)
p = pyaudio.PyAudio()       

def calculate_decibels(data):
    numpy_data = np.frombuffer(data, dtype=np.int16)
    
    # Normalize the data to prevent overflow
    numpy_data = numpy_data / np.max(np.abs(numpy_data), axis=0)

    if numpy_data.size == 0:
        return -np.inf

    rms = np.sqrt(np.mean(numpy_data**2))

    if np.isnan(rms) or rms <= 0:
        return -np.inf

    decibels = 20 * np.log10(rms)
    return decibels

def find_device_index(p, device_name):
    for i in range(p.get_device_count()):
        if device_name in p.get_device_info_by_index(i).get('name'):
            return i
    return None

# Start streaming and recognize speech
def Listen():                                              
    full_text = ''
    while not keyboard.is_pressed(' '):
        pass
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=48000, input=True, frames_per_buffer=2048)
    # stream1 = p.open(format=pyaudio.paInt16, channels=1, rate=48000, input=True,
    #              frames_per_buffer=2048)
    # stream2 = p.open(format=pyaudio.paInt16, channels=1, rate=48000, input=True,
    #              frames_per_buffer=2048)
    try:
        while True:
            data = stream.read(2048, False)  # read in chunks of 2048 bytes
            # data1 = stream1.read(2048)
            # data2 = stream2.read(2048)
            # # Calculate and print decibel levels for both
            # decibels1 = calculate_decibels(data1)
            # decibels2 = calculate_decibels(data2)
            # x_difference = decibels1 - decibels2

            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
            else:
                res = json.loads(rec.PartialResult())
            if not keyboard.is_pressed(' '):
                break
    finally:
        stream.stop_stream()
        stream.close()
        # stream1.stop_stream()
        # stream2.stop_stream()
        # stream1.close()
        # stream2.close()
        return json.loads(rec.FinalResult())['text']

# while True:
#      funi = Listen()
#      print(funi)