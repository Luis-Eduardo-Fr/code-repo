#include <stdio.h>
#include <vlc/vlc.h>

int main(int argc, char* argv[]) {
    libvlc_instance_t * inst;
    libvlc_media_player_t *mp;
    libvlc_media_t *m;

    // Carregar a biblioteca VLC
    inst = libvlc_new(0, NULL);

    // Criar um novo item de mídia
    m = libvlc_media_new_path(inst, "/home/lefds/fnafsl_song.mp4");

    // Criar um novo player de mídia
    mp = libvlc_media_player_new_from_media(m);

    // Não precisa mais da mídia
    libvlc_media_release(m);

    // Reproduzir o vídeo
    libvlc_media_player_play(mp);

    // Aguardar até que a reprodução termine
    while(libvlc_media_player_is_playing(mp)) {}

    // Limpar
    libvlc_media_player_release(mp);
    libvlc_release(inst);

    return 0;
}
