import threading
import queue
from player.player import Player
import sys

class AudioController:
    def __init__(self):
        self.player = Player()
        self.command_queue = queue.Queue()
        self.running = True

    def play_audio(self, file_path):
        threading.Thread(target=self.player.play, args=(file_path,), daemon=True).start()
        print(f"\n▶ Playing {file_path} (commands: pause/resume/stop/status)")
        while self.running:
            try:
                cmd = self.command_queue.get(timeout=0.1)
                if cmd == "pause":
                    self.player.pause()
                    print("⏸ Paused")
                elif cmd == "resume":
                    self.player.resume() # Resume playback
                    print("▶ Resumed")
                elif cmd == "stop":
                    self.player.stop()
                    self.stop_all()
                    print("⏹ Stopped")
                    break
                elif cmd == "status":
                    state = self.player.get_state()
                    print(f"\nCurrent status: {state.name}")
                elif cmd == "exit":
                    self.stop_all()
                    break
            except queue.Empty:
                continue

    def stop_all(self):
        self.running = False
        self.player.stop()

def input_listener(controller):
    while controller.running:
        try:
            cmd = input().strip().lower()
            controller.command_queue.put(cmd)
            if cmd == "exit":
                break
        except (EOFError, KeyboardInterrupt):
            controller.stop_all()
            break

if __name__ == "__main__":
    controller = AudioController()
    
    # Start audio thread
    audio_thread = threading.Thread(
        target=controller.play_audio,
        args=("test.mp3",),
        daemon=True
    )
    audio_thread.start()

    # Start input listener in main thread
    input_listener(controller)

    # Cleanup
    controller.stop_all()
    audio_thread.join()
    print("Player shutdown complete")