import pyaudio

pa = pyaudio.PyAudio()
CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 5
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

def list_devices():
    for i in range(pa.get_device_count()):
        device = pa.get_device_info_by_index(i)

        if device['maxInputChannels'] > 0:
            print(f"\nInput Device {i}: {device['name']}\nSample Rate: {device['defaultSampleRate']}")




def terminate_audio():
    pa.terminate()