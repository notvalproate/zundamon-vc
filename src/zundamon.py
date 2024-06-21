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
        record.start()

        stop = Thread(target=self.wait_for_stop_thread)
        stop.start()

        record.join()
        stop.join()


    def start_app(self, args):
        if(len(args) < 2):
            print("Invalid number of arguments. Please atleast provide the device index after 'start'.")
            return

        device_index = None

        try:
            device_index = int(args[1])
        except ValueError:
            print("Invalid device index. Please use 'list' to list available devices.")
            return
    
        if not self.recorder.is_valid_index(device_index):
            print("Invalid device index. Please use 'list' to list available devices.")
            return
            
        print(f"Recording from device {device_index}")  

        self.run_threads(device_index)        
