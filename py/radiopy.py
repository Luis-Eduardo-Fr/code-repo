from typing import cast
import vlc
import time
import os
import platform
import subprocess
import requests
from colorama import init, Fore, Style



def verify_net():
    try:
        requests.get("https://www.google.com", timeout=5)
    except Exception:
        print(Fore.RED + "Conecte seu computador a internet antes de continuar.." + Style.RESET_ALL)
        exit() 



def verify_os():
    if platform.system() == 'Linux':
        host_platform = 'GNU/LINUX'
        print("Sistema" + Fore.RED + " " + host_platform + " " + Style.RESET_ALL + "detectado, adaptando o programa", end = '', flush = True)
        for _ in range(3):
            time.sleep(0.3)
            print('.', end = '', flush = True)
            time.sleep(0.3)
        os.system('clear')
        print("RADIOPY by lefds" + Fore.RED + " Linux Edition" + Style.RESET_ALL + " " + version)
        get_info_linux()
    elif platform.system() == 'Windows':
        host_platform = 'WINDOWS'
        print("Sistema" + Fore.BLUE + " " + host_platform + " " + Style.RESET_ALL + "detectado, adaptando o programa", end = '', flush = True)
        for _ in range(3):
            time.sleep(0.3)
            print('.', end = '', flush = True)
            time.sleep(0.3)
        os.system('cls')
        print("RADIOPY by lefds" + Fore.BLUE + " Windows Edition" + Style.RESET_ALL + " " + version)
        get_info_win()

def get_info_linux():
    ui = input("Digite a estação: ")
    while len(ui) == 0:
        get_info_linux()
    if ui.lower() in ['acustica', 'acústica']:
        radio_name, radio_url = 'Acústica FM 97.7MHz', 'https://live.virtualcast.com.br/acusticacamaqua' 
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end = '', flush=True)
            time.sleep(0.5)
        print(Fore.GREEN + " Encontrada" + Style.RESET_ALL + "!", end = '', flush=True)
        time.sleep(1.5)
        play_radio_linux(radio_name, radio_url)
    elif ui.lower() in ['gaucha', 'gaúcha']: 
        radio_name, radio_url = 'Gaúcha FM 93.7MHz', 'https://liverdgaupoa.rbsdirect.com.br/primary/gaucha_rbs.sdp/chunklist_36c916a3-44bd-4777-ac8e-2805b97d216b.m3u8'
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)
        for _ in range(3):
            time.sleep(0.3)
            print(".", end = '', flush=True)
            time.sleep(0.3)
        print(Fore.GREEN + " Encontrada!" + Style.RESET_ALL, end = '', flush=True)
        time.sleep(0.7)
        play_radio_linux(radio_name, radio_url)
    else:
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)
        for _ in range(3):
            time.sleep(0.3)
            print(".", end = '', flush=True)
            time.sleep(0.3)
        loop_input = input(Fore.RED +" Estação não encontrada" + Style.RESET_ALL + "!" + "\nTentar novamente?: ")
        if loop_input in ['s', 'sim', 'y', 'yes' 'claro', 'obv']:
            get_info_linux()
        elif loop_input in ['n', 'nao', 'não', 'no']:
            print("Tchau!")
            
        


def play_radio_linux(radio_name, radio_url):
    try:
        os.system('clear')
        print(f"Tocando a \033[1;33m{radio_name}\033[0m!")
        print("Pressione 'CTRL+C' para parar a reprodução..")
        subprocess.run(['mpv', radio_url], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.SubprocessError:
        os.system('clear')
        print(Fore.RED + "Houve um erro durante a reprodução da estação, consulte o PODEROSO lefds" + Style.RESET_ALL)



def get_info_win():
    ui = input("Digite a estação: ")
    while len(ui) == 0:
        get_info_win()
    if ui.lower() in ['acustica', 'acústica']:
        radio_name, radio_url = 'Acústica FM 97.7MHz', 'https://live.virtualcast.com.br/acusticacamaqua' 
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)
        time.sleep(0.8)
        print(".", end = '', flush=True)
        time.sleep(0.8)
        print(".", end = '', flush=True)
        time.sleep(0.8)
        print(".", end = '', flush=True)
        time.sleep(0.8)
        print(Fore.GREEN + "Encontrada!" + Style.RESET_ALL, end = '', flush=True)
        time.sleep(1.5)
        play_radio_win(radio_name, radio_url)
    elif ui.lower() in ['gaucha', 'gaúcha']: 
        radio_name, radio_url = 'Gaúcha FM 93.7MHz', 'https://liverdgaupoa.rbsdirect.com.br/primary/gaucha_rbs.sdp/chunklist_36c916a3-44bd-4777-ac8e-2805b97d216b.m3u8'
        play_radio_win(radio_name, radio_url)
    else:
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)
        time.sleep(0.3)
        print(".", end = '', flush=True)
        time.sleep(0.3)
        print(".", end = '', flush=True)
        time.sleep(0.3)
        print(".", end = '', flush=True)
        time.sleep(0.3)
        loop_input = input(Fore.RED +" Estação não encontrada" + Style.RESET_ALL + "!" + "\nTentar novamente?: ")
        if loop_input in ['s', 'sim', 'y', 'yes' 'claro', 'obv']:
            get_info_win()
        elif loop_input in ['n', 'nao', 'não', 'no']:
            print("Tchau!")
 


def play_radio_win(radio_name, radio_url):
    os.system('cls')
    instance = cast(vlc.Instance, vlc.Instance('--quiet'))
    media = instance.media_new(radio_url)
    player = instance.media_player_new()
    player.set_media(media)
    print("Tocando a " + Fore.YELLOW + radio_name + Style.RESET_ALL + "!")
    try:
        player.play()
        input("Pressione Enter para parar a reprodução..")
        player.stop()
    except Exception:
        os.system('cls')
        print(Fore.RED + "Houve um erro durante a reprodução da estação, consulte o PODEROSO lefds" + Style.RESET_ALL)




######################################################################################################
#
##   RadioPY by lefds
#
##   ALPHA 0.0.1
##   ALPHA 0.0.2 -- Added Net-check
#

version = 'ALPHA 0.0.2'


# Iniciando o colorama
init()

# Verifica se o usuário está conectado a internet
verify_net()

# Verifica o Sistema Host
verify_os()

# O resto do código perdura em funções que são chamadas dentro da função mãe (verify_os),
# refatorações podem (e provavelmente serão) feitas posteriormente...
