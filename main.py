# Python script to launch Roblox Player and Roblox Studio on prompt

from os import getenv, walk
from sys import argv
from time import sleep
from msvcrt import getch
from subprocess import Popen, CalledProcessError
from typing import Optional

ROOT_FOLDER : str = f"{getenv('LOCALAPPDATA')}\\Roblox\\Versions"
CLIENT_FILENAME : str = "RobloxPlayerBeta.exe"
STUDIO_FILENAME : str = "RobloxStudioBeta.exe"

DEFAULT = {}
DEFAULT["no_studio"] = True
DEFAULT["timeout"] = 1.5

no_studio: bool = DEFAULT["no_studio"]
timeout: float = DEFAULT["timeout"]

def str_to_bool(value: str) -> bool:
    value = value.lower()
    truthy = [ "true", "on", "do", "yes", "1" ]

    for _value in truthy:
        if value.startswith(_value):
            if _value == "do" and value.endswith("t"):
                break

            return True
    
    return False

try:
    no_studio = str_to_bool(argv[1])
except IndexError:
    no_studio = DEFAULT["no_studio"]
del str_to_bool

try:
    timeout = float(argv[2])
except (IndexError, ValueError):
    pass

def location_of(filename: str) -> Optional[str]:
    for root, folders, files in walk(ROOT_FOLDER):
        if filename in files:
            return f"{root}\\{filename}"

if __name__ == "__main__":
    client_path = location_of(CLIENT_FILENAME)
    studio_path = location_of(STUDIO_FILENAME)

    progs = [ client_path, studio_path ]

    if no_studio:
        progs.remove(studio_path)
    
    for prog in progs:
        try:
            Popen(prog)
            print(f"Ran: {prog}")
        except CalledProcessError as err:
            print(f"Cannot call: {prog}\nReturn: {err.returncode}\nError: {err.output}")
    
    sleep(timeout)
    exit()
