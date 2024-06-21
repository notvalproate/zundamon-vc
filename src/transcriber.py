import os
import zipfile
import json
import unicodedata as ud
from queue import Queue

import wget
from vosk import Model, KaldiRecognizer

from recorder import FRAME_RATE

MODEL_NAME = 'vosk-model-ja-0.22'
MODEL_URL = F'https://alphacephei.com/vosk/models/{MODEL_NAME}.zip'
MODEL_FOLDER = os.path.abspath('models')
MODEL_PATH = os.path.join(MODEL_FOLDER, MODEL_NAME)
MODEL_ZIP = f'{MODEL_PATH}.zip'


def custom_bar(current, total, width=80):
    print(f'Downloading Model: {round(current / total * 100, 2):6.2f}% [{current:>{len(str(total))}d} / {total}] bytes', end='\r')


class Transcriber:
    def __init__(self, run_app_queue):
        print(MODEL_PATH)

        if(not os.path.exists(MODEL_PATH)):
            print("Model not found! Downloading...\n")
            self.download_and_extract_model()
            print("\nModel downloaded!\n")

        self.run_app_queue = run_app_queue
        self.transcriptions = Queue()
        self.model = Model(MODEL_PATH)
        self.rec = KaldiRecognizer(self.model, FRAME_RATE)
        self.rec.SetWords(True)

    
    def download_and_extract_model(self):
        if not os.path.exists(MODEL_FOLDER):
            os.makedirs(MODEL_FOLDER)

        wget.download(url=MODEL_URL, out=MODEL_FOLDER, bar=custom_bar)

        print("Extracting Model...")

        with zipfile.ZipFile(MODEL_ZIP, 'r') as zip_ref:
            zip_ref.extractall(MODEL_FOLDER)
        
        os.remove(MODEL_ZIP)
        
        print("Finished extracting!")


    def transcribe_recordings(self, recordings):
        while not self.run_app_queue.empty():
            if not recordings.empty():
                frames = recordings.get()

                self.rec.AcceptWaveform(b''.join(frames))
                result = self.rec.Result()
                text = json.loads(result)['text']

                print(f"Text: {ud.normalize('NFC', text).replace(' ', '')}")
