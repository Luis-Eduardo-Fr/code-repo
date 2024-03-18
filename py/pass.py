import vlc
from typing import cast
import time

instance = cast(vlc.Instance, vlc.Instance('--quiet'))
if instance is None:
    print("error")
    exit()
player = instance.media_player_new()
if player is None:
    print("error")
    exit()
media = instance.media_new('/home/lefds/fnafsl_song.mp4')
if media is None:
    print("error")
    exit()
player.set_media(media)
player.play()

while player.is_playing:
    time.sleep(1)
    













