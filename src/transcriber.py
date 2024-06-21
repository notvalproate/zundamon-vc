from queue import Queue
from threading import Thread

class Transcriber:
    def __init__(self, run_app_queue):
        self.run_app_queue = run_app_queue
        self.transcriptions = Queue()
    
    def transcribe_audio(self, recordings):
        pass