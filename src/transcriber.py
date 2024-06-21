import os
from queue import Queue

import wget
from vosk import Model, KaldiRecognizer

MODEL_NAME = 'vosk-model-ja-0.22'
MODEL_URL = F'https://alphacephei.com/vosk/models/{MODEL_NAME}.zip'
MODEL_FOLDER = os.path.abspath('models')
MODEL_PATH = os.path.join(MODEL_FOLDER, MODEL_NAME)

def custom_bar(current, total, width=80):
    print(f'Downloading Model: {round(current / total * 100, 2):6.2f}% [{current:>{len(str(total))}d} / {total}] bytes', end='\r')

class Transcriber:
    def __init__(self, run_app_queue):
        print(MODEL_PATH)

        if(not os.path.exists(MODEL_PATH)):
            print("Model not found! Downloading model...\n")
            self.download_and_extract_model()
            print("\nModel downloaded!")

        self.run_app_queue = run_app_queue
        self.transcriptions = Queue()
        self.model = Model(MODEL_PATH)
    
    
    def download_and_extract_model(self):
        wget.download(url=MODEL_URL, out=MODEL_FOLDER, bar=custom_bar)


    def transcribe_recordings(self, recordings):
        while not self.run_app_queue.empty():
            if not recordings.empty():
                recording = recordings.get()
                print(f"Transcribing {len(recording)} frames")
