import wave

import requests

VOICEVOX_API_URL = 'http://localhost:50021'

# For Testing
import pyaudio
from io import BytesIO

class Synthesizer:
    def __init__(self):
        try:
            requests.get(VOICEVOX_API_URL)
        except requests.exceptions.ConnectionError:
            print("Voicevox server is not running. Please start the VOICEVOX Engine.\nInstall it from https://voicevox.hiroshiba.jp/")
            exit(1)
        
        self.p = pyaudio.PyAudio()
        self.virtual_audio_cable_index = self.get_virtual_audio_cable_index()


    def get_virtual_audio_cable_index(self):
        for i in range(self.p.get_device_count()):
            if 'CABLE Input (VB-Audio Virtual ' in self.p.get_device_info_by_index(i)['name']:
                return i

        return None


    def play_audio_through_vb_cable(self, audio):
        audio_file = BytesIO(audio)
        wav_file = wave.open(audio_file, 'rb')

        stream = self.p.open(format=self.p.get_format_from_width(wav_file.getsampwidth()),
                channels=wav_file.getnchannels(),
                rate=wav_file.getframerate(),
                output=True,
                output_device_index=self.virtual_audio_cable_index)
        
        chunk = 1024
        data = wav_file.readframes(chunk)

        while data:
            stream.write(data)
            data = wav_file.readframes(chunk)
        
        stream.stop_stream()
        stream.close()
        
        wav_file.close()


    def get_audio_query(self, text):
        params = { 'text': text, 'speaker': 1 }
        response = requests.post(f'{VOICEVOX_API_URL}/audio_query', params=params)
        return response.text
    

    def synthesize_to_audio(self, audio_query):
        params = { 'speaker': 1 }
        response = requests.post(f'{VOICEVOX_API_URL}/synthesis', params=params, data=audio_query)
        
        print("Playing audio...")
        self.play_audio_through_vb_cable(response.content)


    def synthesize_text(self, text):
        audio_query = self.get_audio_query(text)
        print("Synthesizing...")
        self.synthesize_to_audio(audio_query)

    def __del__(self):
        self.p.terminate()