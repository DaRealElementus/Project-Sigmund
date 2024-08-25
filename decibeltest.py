import pyaudio
import numpy as np

# Constants for the audio stream
CHUNK = 2048  # Number of samples per frame
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Single channel for microphone
RATE = 48000  # Sample rate (samples per second)

# Function to calculate the decibel level from audio data
#def calculate_decibels(data):
    #numpy_data = np.frombuffer(data, dtype=np.int16)
    #rms = np.sqrt(np.mean(numpy_data**2))
    #if rms > 0:
        #decibels = 20 * np.log10(rms)
    #else:
        #decibels = -np.inf  # Handle case where RMS is 0
    #return decibels

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

# Initialize PyAudio
p = pyaudio.PyAudio()

# Function to find device index by name
def find_device_index(p, device_name):
    for i in range(p.get_device_count()):
        if device_name in p.get_device_info_by_index(i).get('name'):
            return i
    return None

# Replace 'Mic1' and 'Mic2' with actual names or indices of your microphones
#mic1_device_index = find_device_index(p, '1')
#mic2_device_index = find_device_index(p, 'Primary Sound Capture Driver')

#if mic1_device_index is None or mic2_device_index is None:
    #print("Could not find both microphones.")
    #p.terminate()
    #exit()

# Open streams for each microphone
#stream1 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                 #input_device_index=mic1_device_index, frames_per_buffer=CHUNK)
#stream2 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                 #input_device_index=mic2_device_index, frames_per_buffer=CHUNK)
stream1 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                 frames_per_buffer=CHUNK)
stream2 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                 frames_per_buffer=CHUNK)

print("Recording from both microphones... Press Ctrl+C to stop.")

try:
    while True:
        # Read data from both microphones
        data1 = stream1.read(CHUNK)
        data2 = stream2.read(CHUNK)
        
        # Calculate and print decibel levels for both
        decibels1 = calculate_decibels(data1)
        decibels2 = calculate_decibels(data2)
        x_difference = decibels1 - decibels2
        
        #print(f"Mic1 Decibel Level: {decibels1:.2f} dB - Mic2 Decibel Level: {decibels2:.2f} dB - Difference: {x_difference} dB")
        #print(f"Mic2 Decibel Level: {decibels2:.2f} dB")
except KeyboardInterrupt:
    print("Recording stopped.")
    stream1.stop_stream()
    stream2.stop_stream()
    stream1.close()
    stream2.close()
    p.terminate()
