import requests

VOICEVOX_API_URL = 'http://localhost:50021'

class Synthesizer:
    def __init__(self):
        try:
            requests.get(VOICEVOX_API_URL)
        except requests.exceptions.ConnectionError:
            print("Voicevox server is not running. Please start the VOICEVOX Engine.\nInstall it from https://voicevox.hiroshiba.jp/")
            exit(1)

    def get_audio_query(self, text):
        params = { 'text': text, 'speaker': 1 }
        response = requests.post(f'{VOICEVOX_API_URL}/audio_query', params=params)
        return response.text
    
    def synthesize_to_audio(self, audio_query):
        params = { 'speaker': 1 }
        response = requests.post(f'{VOICEVOX_API_URL}/synthesis', params=params, data=audio_query)
        with open('output.wav', 'wb') as file:
            file.write(response.content)

    def synthesize_text(self, text):
        audio_query = self.get_audio_query(text)

        self.synthesize_to_audio(audio_query)
