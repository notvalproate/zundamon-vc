from recognizer import zundamon_recognizer
from synthesizer import Synthesizer

class Transcriber:
    def __init__(self, run_app_queue):
        self.run_app_queue = run_app_queue
        self.synthesizer = Synthesizer()

    def transcribe_recordings(self, recordings):
        while not self.run_app_queue.empty():
            audio = recordings.get()

            if audio == 'EXIT':
                break

            text = zundamon_recognizer.recognize_whisper(audio_data=audio, model='base', language='ja')

            if text != '' and len(text) < 120 and text != 'ご視聴ありがとうございました' and 'スタッフの音が出てくる' not in text:
                print(f"Transcribed text: {text}")
                self.synthesizer.synthesize_text(text)
