
from player.player import Player
import os
import time
import threading # Initialize the player instance

player = Player()

def command_listener():
    while player.state!= -1:
        try:
            print("Enter command: (play, pause,resume, stop, skip)")
            cmd = input().strip().lower()
            player.queue.put(cmd)
            manage_audio()
            if cmd == "exit":
                break
        except (EOFError, KeyboardInterrupt):
            player.stop()
            break
    print("exiting")

def manage_audio():
    if not player.queue.empty():
        command = player.queue.get()  # Get command from the queue with a timeout
        if command == "play":
            threading.Thread(target=player.play,
                                  args=(media_path,),daemon=True).start()  # playing audiobook on different thread.
        elif command == "pause":
            print("Pausing the audiobook...")
            player.pause()
        elif command == "stop":
            player.stop()
            print("Stopping the audiobook...")
        elif command == "resume":
            print("Resuming the audiobook...")
            player.resume()
        elif command == "skip":
            print("Enter time in seconds to skip the audiobook...")
            cmd = input().strip().lower()
            player.skip(int(cmd))

        else:
            print(f"Unknown command: {command}")
def destroy():
    pass

if __name__ == "__main__":
    media_path = "./test.mp3"
    try:
        command_listener()
    except KeyboardInterrupt:
        pass

