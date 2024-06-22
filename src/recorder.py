from queue import Queue

import speech_recognition as sr

from recognizer import zundamon_recognizer

class Recorder:
    def __init__(self, run_app_queue):
        self.recordings = Queue()
        self.run_app_queue = run_app_queue
    

    def list_devices(self):
        working_mics = sr.Microphone.list_working_microphones()

        print("\nAvailable microphones:")
        for index in working_mics.keys():
            print(f"\nIndex: {index}\nName: {working_mics[index]}\n")


    def is_valid_index(self, index):
        working_mics = sr.Microphone.list_working_microphones()

        if index not in working_mics.keys():
            return False
        
        return True


    def record_microphone(self, index):
        if index is None:
            print("Recording from default device")
        else:
            print(f"Recording from device {index}")

        while not self.run_app_queue.empty():
            with sr.Microphone(device_index=index) as mic:
                try:
                    zundamon_recognizer.adjust_for_ambient_noise(mic, duration=0.25)
                    audio = zundamon_recognizer.listen(mic)
                    self.recordings.put(audio)
                except sr.UnknownValueError:
                    print("Could not understand audio")

        self.recordings.put('EXIT')