import vlc
import time

media = vlc.MediaPlayer('/home/lefds/fnafsl_song.mp4')
media.play()
while True:
    time.sleep(1)
    if not media.is_playing():
            break

