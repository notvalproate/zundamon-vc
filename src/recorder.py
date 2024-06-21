from queue import Queue
from threading import Thread

import pyaudio

CHANNELS = 1
FRAME_RATE = 16000
RECORD_DURATION_SECONDS = 5
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

class Recorder:
    def __init__(self, run_app_queue):
        self.pa = pyaudio.PyAudio()
        self.recordings = Queue()
        self.run_app_queue = run_app_queue
    

    def list_devices(self):
        for i in range(self.pa.get_device_count()):
            device = self.pa.get_device_info_by_index(i)

            if device['maxInputChannels'] > 0:
                print(f"\nInput Device {i}: {device['name']}\nSample Rate: {device['defaultSampleRate']}")


    def is_valid_index(self, index):
        if index < 0 and index >= self.pa.get_device_count():
            return False
        
        device = self.pa.get_device_info_by_index(index)

        if(device['maxInputChannels'] <= 0):
            return False
        
        return True


    def record_microphone(self, index, chunk=1024):
        stream = self.pa.open(format=AUDIO_FORMAT,
                        channels=CHANNELS,
                        rate=FRAME_RATE,
                        input=True,
                        input_device_index=index,
                        frames_per_buffer=chunk)
        
        frames = []

        while not self.run_app_queue.empty():
            data = stream.read(chunk)
            frames.append(data)

            if len(frames) >= (FRAME_RATE * RECORD_DURATION_SECONDS) / chunk:
                self.recordings.put(frames.copy())
                frames.clear()

        stream.stop_stream()
        stream.close()


    def __del__(self):
        self.pa.terminate()