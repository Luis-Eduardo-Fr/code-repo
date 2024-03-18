import os
import sys
import subprocess
import time
def req_check():
    try:
        subprocess.run(['mpv', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if os.getuid() == 0:
            print("\033[1;31mYou must not run it as root.\033[0m")
            sys.exit()

    except subprocess.CalledProcessError:
        print("\033[1;31mMPV is not installed on your system\033[0m")
        sys.exit()


def radio_found():
    print("Searching in Database", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print("\033[1;32m FOUND!\033[0m")
    time.sleep(2)
    os.system('clear')


def radio_not_found():
    print("Searching in Database", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print(".", end='', flush=True)
    time.sleep(1)
    print("\033[1;32m NOT FOUND!\033[0m")
    time.sleep(2)
    os.system('clear')
    os.system('python /home/lefds/code/py/radio.py')


def mpv_play():
    question = ''
    while len(question) == 0:
        question = input("Type a radio: ")

    if question.lower() in ["acustica", "acústica"]:
        radio_id, radio_url = "Acústica FM 97.7MHz", "https://live.virtualcast.com.br/acusticacamaqua"
        radio_found()
        print(f'Playing \033[1;33m{radio_id}\033[0m')
        print("Press \033[1;31m'CTRL+C'\033[0m to quit. ")
        subprocess.run(['mpv', radio_url ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    elif question in ["gaucha", "gaúcha"]:
        radio_id, radio_url = "Gaúcha FM 93.7MHz", "https://liverdgaupoa.rbsdirect.com.br/primary/gaucha_rbs.sdp/chunklist_36c916a3-44bd-4777-ac8e-2805b97d216b.m3u8"
        radio_found()
        print(f'Playing \033[1;33m{radio_id}\033[0m')
        print("Press \033[1;31m'CTRL+C'\033[0m to quit. ")
        subprocess.run(['mpv', radio_url ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    else:
        radio_not_found()


req_check()
mpv_play()
