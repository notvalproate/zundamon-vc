import pyaudio

CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 5
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

class Recorder:
    def __init__(self):
        self.pa = pyaudio.PyAudio()
    
    def list_devices(self):
        for i in range(self.pa.get_device_count()):
            device = self.pa.get_device_info_by_index(i)

            if device['maxInputChannels'] > 0:
                print(f"\nInput Device {i}: {device['name']}\nSample Rate: {device['defaultSampleRate']}")

    def record_microphone(self, index, chunk):
        stream = self.pa.open(format=AUDIO_FORMAT, 
                        channels=CHANNELS, 
                        rate=FRAME_RATE, 
                        input=True,
                        input_device_index=index,
                        frames_per_buffer=chunk)
        
        frames = []

    def __del__(self):
        self.pa.terminate()