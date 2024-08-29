import vosk
import pyaudio
import json
import pygame

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))  # Needed to capture events

# Initialize the model with model-path
model = vosk.Model(lang="en-us")

rec = vosk.KaldiRecognizer(model, 48000)
p = pyaudio.PyAudio()       

def is_space_pressed():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
    keys = pygame.key.get_pressed()
    return keys[pygame.K_SPACE]

# Start streaming and recognize speech
def Listen():                                              
    full_text = ''              
    while not is_space_pressed():
        pass
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=48000, input=True, frames_per_buffer=2048)
    
    #try:
    while is_space_pressed():
        data = stream.read(2048, False)  # read in chunks of 2048 bytes
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
        else:
            res = json.loads(rec.PartialResult())
    #finally:
    stream.stop_stream()
    stream.close()
    return json.loads(rec.FinalResult())['text']

#while True:
#    result = Listen()
#    print(result)