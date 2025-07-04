import vlc
import threading
import queue
import sys

# --- Audio Player Class ---
class AudiobookPlayer:
    def __init__(self, file_path):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.player.set_media(self.instance.media_new(file_path))
        self.command_queue = queue.Queue()
        self.is_running = True

    def play(self):
        self.player.play()
        print("▶ Playing (Commands: stop/pause/translate)")

    def pause(self):
        self.player.pause()
        print("⏸ Paused")

    def stop(self):
        self.player.stop()
        self.is_running = False
        print("⏹ Stopped")

    def translate(self):
        print("🔊 Translating current segment... (mock)")

# --- Command Handler (Runs in Background) ---
def command_listener(player):
    while player.is_running:
        cmd = input().strip().lower()  # Wait for user input
        player.command_queue.put(cmd)

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python player.py <audiobook.mp3>")
        sys.exit(1)

    player = AudiobookPlayer(sys.argv[1])
    player.play()

    # Start command listener thread
    threading.Thread(target=command_listener, args=(player,), daemon=True).start()

    # Main playback loop
    try:
        while player.is_running:
            if not player.command_queue.empty():
                cmd = player.command_queue.get()
                if cmd == "stop":
                    player.stop()
                elif cmd == "pause":
                    player.pause()
                elif cmd == "translate":
                    player.translate()
                elif cmd == "play":
                    player.play()
                else:
                    print("Unknown command (try: stop/pause/translate)")
    except KeyboardInterrupt:
        player.stop()