from queue import Queue

import speech_recognition as sr

from recognizer import zundamon_recognizer

class Recorder:
    def __init__(self, run_app_queue):
        self.recordings = Queue()
        self.run_app_queue = run_app_queue
    

    def list_devices(self):
        working_mics = sr.Microphone.list_working_microphones()

        print("\nAvailable microphones:\n")
        for index in working_mics.keys():
            print(f"\nIndex: {index} - {working_mics[index]}\n")


    def is_valid_index(self, index):
        working_mics = sr.Microphone.list_working_microphones()

        if index not in working_mics.keys():
            return False
        
        return True


    def record_microphone(self, index):
        print(f"Recording from device {index}")

        while not self.run_app_queue.empty():
            with sr.Microphone(device_index=index) as mic:
                try:
                    zundamon_recognizer.adjust_for_ambient_noise(mic, duration=0.4)
                    audio = zundamon_recognizer.listen(mic)
                    self.recordings.put(audio)
                except sr.UnknownValueError:
                    print("Could not understand audio")