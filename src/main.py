import sys
from threading import Thread
from queue import Queue

from zundamon import Zundamon

app = Zundamon()

if __name__ == '__main__':
    command_args = sys.argv[1:]

    if len(command_args) == 0:
        print("Invalid command. Please use 'start' to start recording.")
        sys.exit(1)

    command = command_args[0]

    if command == 'start':
        app.start_app(command_args)
    elif command == 'list':
        app.recorder.list_devices()
    else:
        print("Invalid command. Please use 'start' to start recording.")