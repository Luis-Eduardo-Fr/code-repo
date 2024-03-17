from typing import cast
import vlc
#if os.getuid() == 0:
    #print("Esse programa não deve ser reproduzido com usuário root.")

print("RADIOPY BY lefds")

def get_info():
    ui = input("Digite a estação: ")
    while len(ui) == 0:
        get_info()

    if ui.lower() in ['acustica', 'acústica']:
        radio_name, radio_url = 'Acústica FM 97.7MHz', 'https://live.virtualcast.com.br/acusticacamaqua'
        play_radio(radio_name, radio_url)
    elif ui.lower() in ['gaucha', 'gaúcha']:
        radio_name, radio_url = 'Gaúcha FM 93.7MHz', 'https://liverdgaupoa.rbsdirect.com.br/primary/gaucha_rbs.sdp/chunklist_36c916a3-44bd-4777-ac8e-2805b97d216b.m3u8'
        play_radio(radio_name, radio_url)



def play_radio(radio_name, radio_url):
        instance = cast(vlc.Instance, vlc.Instance('--quiet'))
        media = instance.media_new(radio_url)
        print("Media:")
        player = instance.media_player_new()
        player.set_media(media)
        print(f"Tocando a \033[1;33m{radio_name}\033[0m!")
        player.play()
        input("Pressione Enter para parar a reprodução..")
        player.stop()

get_info()


