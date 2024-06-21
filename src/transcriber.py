from queue import Queue

class Transcriber:
    def __init__(self, run_app_queue):
        self.run_app_queue = run_app_queue
        self.transcriptions = Queue()
    
    def transcribe_audio(self, recordings):
        while not self.run_app_queue.empty():
            if not recordings.empty():
                recording = recordings.get()
                print(f"Transcribing {len(recording)} frames")
                