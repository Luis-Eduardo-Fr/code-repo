import requests
import platform
import os
import sys
from colorama import Fore, Style

def verification(host_os):
    try:
        requests.get('https://www.google.com', timeout=5) # Check Internet connection
    except Exception:
        print(Fore.RED + "Connect your PC to the internet before continuing." + Style.RESET_ALL)
        sys.exit()
    
    if platform.system() == 'Linux':
        host_os = 'GNU/LINUX' # Assign value to host_os
        version = ''
        print("RADIOPY by lefds" + Fore.RED + " Linux Edition" + Style.RESET_ALL + " " + version) # Assuming version is defined
        if os.getuid() == 0:
            print(Fore.RED + "This script should not be run as superuser (root)." + Style.RESET_ALL)
            sys.exit()
        if not os.path.exists('/usr/bin/mpv') and not os.path.exists('/usr/local/bin/mpv'):
            print(Fore.RED + "ERROR: MPV is not installed." + Style.RESET_ALL)
            sys.exit()
    
    # You can add more conditions for other OS types here
    return host_os

# Assuming station_id is defined
host_os = verification(None)

if host_os == 'GNU/LINUX':
    print("Ih mano existe não")
