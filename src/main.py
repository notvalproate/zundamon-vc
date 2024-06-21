import sys
from threading import Thread
from queue import Queue

from audio import Recorder

recorder = Recorder()

def start_recording(command_args):
    if(len(command_args) != 2):
        print("Invalid number of arguments. Please provide only the device index after 'start'.")
        return

    device_index = None

    try:
        device_index = int(command_args[1])
    except ValueError:
        print("Invalid device index. Please use 'list' to list available devices.")
        return

    if recorder.is_valid_index(device_index):
        print(f"Recording from device {device_index}")
        recorder.record_microphone(device_index)
    else:
        print("Invalid device index. Please use 'list' to list available devices.")


if __name__ == '__main__':
    command_args = sys.argv[1:]

    if len(command_args) == 0:
        print("Invalid command. Please use 'start' to start recording.")
        sys.exit(1)
        
    command = command_args[0]

    if command == 'start':
        start_recording(command_args=command_args)
    elif command == 'list':
        recorder.list_devices()
    else:
        print("Invalid command. Please use 'start' to start recording.")