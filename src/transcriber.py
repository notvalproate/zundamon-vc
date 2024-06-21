import unicodedata as ud
from queue import Queue

from recognizer import zundamon_recognizer

class Transcriber:
    def __init__(self, run_app_queue):
        self.run_app_queue = run_app_queue
        self.transcriptions = Queue()

    def transcribe_recordings(self, recordings):
        while not self.run_app_queue.empty():
            if not recordings.empty():
                audio = recordings.get()
                text = zundamon_recognizer.recognize_whisper(audio_data=audio, model='medium', language='ja')
                if not text == 'ご視聴ありがとうございました':
                    self.transcriptions.put(text)
