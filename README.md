#  zundamon-vc

A voice changer that uses the VOICEVOX engine to convert your speech into zundamon's voice as input!
## Installation
- Clone the repository: `git clone https://github.com/notvalproate/zundamon-vc`
- Create a new virtual environment: `python -m venv venv`
- Activate the venv: `./venv/Scripts/activate`
- Install the packages: `pip install -r requirements.txt`
- Install [VOICEVOX](https://voicevox.hiroshiba.jp/)
- Install [VB-Audio Virtual Cable](https://vb-audio.com/Cable/)
## Usage
- Go to your application of choice, and select `CABLE Output (VB-Audio Virtual Cable)` as the input device.
- Activate the venv: `./venv/Scripts/activate`
- Run command: `python ./src/main.py [command]`
## Commands:
### 1. `list`
- **Description:** Provides a list of all the input devices available with their indexes <br>
- **Usage:** `python ./src/main.py list`
### 2. `start`
- **Description:** Starts the application and listens to your microphone for speech, transcripts, synthesizes, and plays it back into the virtual cable input device.<br>
- **Usage:** `python ./src/main.py start [INDEX]`<br>
- q**Parameters:** [INDEX] Optional parameter to specify the input device index. If not provided, default input device is used.
