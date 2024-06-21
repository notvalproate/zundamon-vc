from queue import Queue
from threading import Thread

import readchar

from recorder import Recorder
from transcriber import Transcriber

class Zundamon:
    def __init__(self):
        self.run_app = Queue()
        self.recorder = Recorder(self.run_app)
        self.transcriber = Transcriber(self.run_app)
    

    def wait_for_stop_thread(self):
        print("Press Any Key to stop recording...")
        readchar.readchar()
        self.run_app.get()


    def run_threads(self, index):
        self.run_app.put(True)

        record = Thread(target=self.recorder.record_microphone, args=(index,))
        transcribe = Thread(target=self.transcriber.transcribe_recordings, args=(self.recorder.recordings,))
        stop = Thread(target=self.wait_for_stop_thread)

        record.start()
        transcribe.start()
        stop.start()

        stop.join()
        transcribe.join()
        record.join()


    def start_app(self, args):
        device_index = None

        try:
            device_index = int(args[1])
            if not self.recorder.is_valid_index(device_index):
                print("Invalid device index. Please use 'list' to list available devices.")
                return
        except Exception:
            pass
    
        self.run_threads(device_index)        
