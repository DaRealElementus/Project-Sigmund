import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import vosk
import pyaudio
import json
import keyboard

# Configuration parameters
SAMPLE_RATE = 16000    # Sample rate of the audio for direction detection
DURATION = 5           # Duration of audio recording in seconds
SPEED_OF_SOUND = 343.2 # Speed of sound in m/s
DISTANCE = 1           # Assume a distance of 1 meter for simplicity

# Initialize Vosk model
model = vosk.Model(lang="en-us")
rec = vosk.KaldiRecognizer(model, 48000)
p = pyaudio.PyAudio()

# Function to detect sound direction using cross-correlation
def detect_sound_direction(audio_data):
    # Process the audio to find sound source direction using cross-correlation
    n = len(audio_data)
    X = np.fft.rfft(audio_data[:, 0])
    X_conj = np.conj(X)
    P = X * X_conj
    P[P == 0] = 1e-6  # To avoid division by zero

    phi = np.fft.irfft(P / np.abs(P))
    lags = np.arange(-n // 2, n // 2)

    # Find the lag with the maximum correlation
    max_corr_idx = np.argmax(np.abs(phi))
    max_corr_lag = lags[max_corr_idx]

    # Convert lag to angle of arrival
    arg = max_corr_lag * SPEED_OF_SOUND / (SAMPLE_RATE * DISTANCE)
    
    # Clamp the value of arg to the range [-1, 1] to prevent arcsin from failing
    arg = np.clip(arg, -1, 1)

    angle_of_arrival = np.arcsin(arg)

    print(f"Estimated Angle of Arrival: {np.degrees(angle_of_arrival)} degrees")

    # Plot the correlation results (optional, for debugging)
    plt.figure(figsize=(10, 4))
    plt.plot(lags, np.abs(phi))
    plt.title('Generalized Cross-Correlation')
    plt.xlabel('Lag')
    plt.ylabel('Correlation')
    plt.show()

    return np.degrees(angle_of_arrival)

# Start streaming and recognize speech
def Listen():
    full_text = ''
    
    print("Press and hold 'Space' to start listening...")
    while not keyboard.is_pressed(' '):
        pass
    print("Listening...")

    # Record audio
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float64')
    sd.wait()
    print("Recording complete.")

    # Detect sound direction
    angle_of_arrival = detect_sound_direction(audio)

    # Convert recorded audio to bytes for Vosk recognition
    audio_bytes = (audio * 32767).astype(np.int16).tobytes()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=48000, input=True, frames_per_buffer=2048)

    try:
        while True:
            data = stream.read(2048, False)  # read in chunks of 2048 bytes
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                print(f"Recognized Text: {res['text']}")
            else:
                res = json.loads(rec.PartialResult())
                print(f"Partial Recognition: {res['partial']}")
            
            if not keyboard.is_pressed(' '):
                break
    finally:
        stream.stop_stream()
        stream.close()
        final_text = json.loads(rec.FinalResult())['text']
        print(f"Final Recognized Text: {final_text}")
        return final_text, angle_of_arrival

# Example usage
if __name__ == "__main__":
    recognized_text, sound_direction = Listen()
    print(f"Recognized Text: {recognized_text}")
    print(f"Sound Direction: {sound_direction} degrees")
