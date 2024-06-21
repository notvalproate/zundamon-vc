

class Synthesizer:
    def __init__(self):
        self.synthesizer = None

    def load(self, synthesizer):
        self.synthesizer = synthesizer

    def synthesize(self, text):
        return self.synthesizer.synthesize(text)