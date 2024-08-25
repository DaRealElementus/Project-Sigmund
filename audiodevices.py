import pyaudio

# Initialize PyAudio
p = pyaudio.PyAudio()

# List all audio devices
print("Available audio devices:")
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    print(f"Device {i}: {device_info['name']} - Input Channels: {device_info['maxInputChannels']}")

p.terminate()
