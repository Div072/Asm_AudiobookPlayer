from player.player import Player
from CLI.commands import manage_audio
player = Player()

if __name__ == "__main__":
    player.player.queue.put("play")
    player.player.queue.put("pause")
    player.player.queue.put("resume")
    player.player.queue.put("skip")



