import sys
from threading import Thread
from queue import Queue

messages = Queue()
recordings = Queue()

def start_recording(data):
    print(data)

if __name__ == '__main__':
    command_args = sys.argv[1:]

    command = command_args[0]

    if command == 'start':
        start_recording("Started transcripting")
    else:
        print("Invalid command. Please use 'start' to start recording.")