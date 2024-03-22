from colorama import init, Fore, Style
from typing import cast
import subprocess
import platform
import requests
#import winreg
import time
import sys
import vlc
import os




def verification(host_os):
    try:
        requests.get('https://www.google.com', timeout=5) # Verifica se a Internet;
    except Exception:
        print(Fore.RED + "Conecte seu PC a internet à internet antes de continuar.." + Style.RESET_ALL)
        sys.exit()
    if platform.system() == 'Linux': # Verifica o sistema do usuário;
        host_os = 'GNU/LINUX'
        print("RADIOPY by lefds" + Fore.RED + " Linux Edition" + Style.RESET_ALL + " " + version)
        if os.getuid() == 0:
            print(Fore.RED + "Este script não deve ser reproduzido como SuperUsuário (ROOT)." + Style.RESET_ALL)
            sys.exit()
        if not os.path.exists("/usr/bin/mpv") and not os.path.exists("/usr/local/bin/mpv"):
            print(Fore.RED + "ERRO: MPV não está instalado." + Style.RESET_ALL)
            sys.exit()


    return host_os
        


def get_input_linux():
    ui = input("Digite a estação: ")
    while len(ui) == 0:
        ui = input("Digite a estação: ")

    if ui.lower() in station[0]:
        station_id = 0
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)
        for _ in range(3):
            time.sleep(0.2)
            print(".", end = '', flush=True)
            time.sleep(0.2)
        print(Fore.GREEN + " Encontrada" + Style.RESET_ALL + "!", end = '', flush=True)
        time.sleep(0.7)
        return True, station_id

    elif ui.lower() in station[1]: 
        station_id = 1
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)

        for _ in range(3):
            time.sleep(0.2)
            print(".", end = '', flush=True)
            time.sleep(0.2)

        print(Fore.GREEN + " Encontrada!" + Style.RESET_ALL, end = '', flush=True)
        time.sleep(0.7)
        return True, station_id
    else:
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)

        for _ in range(3):
            time.sleep(0.3)
            print(".", end = '', flush=True)
            time.sleep(0.3)

        loop_input = input(Fore.RED +" Estação não encontrada" + Style.RESET_ALL + "!" + "\nTentar novamente?: ")
    
        if loop_input in ['s', 'sim', 'y', 'yes' 'claro', 'obv']:
            get_input_linux()

        elif loop_input in ['n', 'nao', 'não', 'no']:
            print("Tchau!")
            sys.exit()
            
        

def play_radio_linux(station_id):
    try:
        os.system('clear')
        print(f"Tocando a \033[1;33m{station_name[station_id]}\033[0m!")
        print("Pressione 'CTRL+C' para parar a reprodução..")
        subprocess.run(['mpv', station_url[station_id]], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.SubprocessError:
        os.system('clear')
        print(Fore.RED + "Houve um erro durante a reprodução da estação, consulte o PODEROSO lefds" + Style.RESET_ALL)


#==========================================================================================================================#
#==========================================================================================================================#


def get_input_win():

    ui = input("Digite a estação: ")
    while len(ui) == 0:
        ui = input("Digite a estação: ")

    if ui.lower() in station[0]:
        station_id = 0
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)
        time.sleep(0.8)
        print(".", end = '', flush=True)
        time.sleep(0.8)
        print(".", end = '', flush=True)
        time.sleep(0.8)
        print(".", end = '', flush=True)
        time.sleep(0.8)
        print(Fore.GREEN + " Encontrada!" + Style.RESET_ALL, end = '', flush=True)
        time.sleep(1.5)
        return True, station_id
                               

    elif ui.lower() in station[1]: 
        station_id = 1
        print(Fore.YELLOW + "Acessando o banco de dados" + Style.RESET_ALL, end = '', flush=True)
        time.sleep(0.8)
        print(".", end = '', flush=True)
        time.sleep(0.8)
        print(".", end = '', flush=True)
        time.sleep(0.8)
        print(".", end = '', flush=True)
        time.sleep(0.8)
        print(Fore.GREEN + " Encontrada!" + Style.RESET_ALL, end = '', flush=True)
        time.sleep(1.5)
        return True, station_id


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
            get_input_win()
        elif loop_input in ['n', 'nao', 'não', 'no']:
            print(Fore.YELLOW + "Programa encerrado." + Style.RESET_ALL)
 


def play_radio_win(station_id):
    os.system('cls')
    instance = cast(vlc.Instance, vlc.Instance('--quiet'))
    media = instance.media_new(station_url[station_id])
    player = instance.media_player_new()
    player.set_media(media)
    print("Tocando a " + Fore.YELLOW + station_name[station_id] + Style.RESET_ALL + "!")
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
##  ALPHA 0.0.1
##  ALPHA 0.0.2 -- Added Net-check.
##  ALPHA 0.0.3 -- Changed stations based on if statements, now in their own lists.
##  ALPHA 0.0.4 -- BIG Changes on code structure, now more human-readable and optimized.
##
#

version = 'ALPHA 0.0.4'

station = ['acustica', 'gaucha', 'grenal']
station_name = ['Acústica FM 97.7MHz', 'Gaúcha FM 93.7MHz', 'Rádio GRENAL 95.9MHz FM']
station_url = ['https://live.virtualcast.com.br/acusticacamaqua', 'https://liverdgaupoa.rbsdirect.com.br/primary/gaucha_rbs.sdp/chunklist_36c916a3-44bd-4777-ac8e-2805b97d216b.m3u8', ]
# Iniciando o colorama
init()

# Verifica todas as dependências necessárias
host_os = verification(None)

if host_os == 'GNU/LINUX':
    sucess, station_id = get_input_linux()
    if sucess:
        play_radio_linux(station_id)

elif host_os == 'WINDOWS':
    sucess, station_id = get_input_win()
    if sucess:
        play_radio_win(station_id)


# O resto do código perdura em funções que são chamadas dentro da função mãe (verify_os),
# refatorações podem (e provavelmente serão) feitas posteriormente...
