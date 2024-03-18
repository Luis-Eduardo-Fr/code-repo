import vlc
import time
import os
from typing import cast

max_wait = 2
wait_time = 0

instance = cast(vlc.Instance, vlc.Instance('--quiet --no-xlib'))
media = instance.media_new('/home/lefds/5.mp4')
player = instance.media_player_new()
player.set_media(media)
player.play()

while player.is_playing:
    time.sleep(1)
    #wait_time += 1
    #if wait_time >= max_wait:
#        break
#instance.release()
#os.kill(player.get_pid(), 9)
    
    

