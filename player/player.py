from math import floor
import vlc

import queue
class Player:
     def __init__(self):
          self.instance = vlc.Instance()
          self.player = self.instance.media_player_new()
          self.queue = queue.Queue()
          self.state = 0  # 0 for pause, -1 for stopped, and 1 for playing
     
     def play(self, media_path: str):
          try:
               """Play the media file."""
               media = self.instance.media_new(media_path)
               self.player.set_media(media)
               self.player.audio_set_volume(100)
               self.player.play()
               self.state = 1
               print("State:", self.player.get_state())


          except Exception as e:
               print(f"An error occurred while trying to play the media: {e}")
          
     def stop(self):
          self.state = -1
          self.player.stop()

     def pause(self):
          self.state = 0
          self.player.pause() 
     def resume(self):  
          current_time = self.player.get_time()  # Get the current playback time  
          self.player.pause()
          self.player.set_time(current_time)  # Set the playback time to where it was paused
          print(f"Resuming playback from {floor(int(current_time/(1000*60)))} min and {floor(int(current_time/1000))} sec")
          self.state = 1
          self.player.play()  # Resume playback by calling play again
          
     def skip(self,time_in_seconds: int):
          current_time = self.player.get_time()
          if time_in_seconds + int(current_time/1000) >= self.player.get_length()/1000:
               print("Skipping beyond the end of the media is not allowed.")
               return
          if time_in_seconds + int(current_time/1000) < 0:
               print("Skipping to a negative time is not allowed.")
               return
          self.player.pause()
          self.player.set_time(current_time + time_in_seconds*1000)
          self.player.play()
