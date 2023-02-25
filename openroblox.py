# Py script to launch Roblox and optionally Roblox Studio
# on Windows boot if script is placed inside ->
# %LOCALAPPDATA%\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

from os import getenv, walk
from sys import argv
from time import sleep
from msvcrt import getch
from subprocess import run, Popen, CompletedProcess, CalledProcessError
from typing import Optional

ROOT_FOLDER : str = f"{getenv('LOCALAPPDATA')}\\Roblox\\Versions"
CLIENT_FILENAME : str = "RobloxPlayerBeta.exe"
STUDIO_FILENAME : str = "RobloxStudioBeta.exe"

# The timeout is really just for debugging
timeout: int

try:
    timeout = int(argv[1])
except (IndexError, ValueError):
    timeout = 0

def location_of(filename: str) -> Optional[str]:
    for root, folders, files in walk(ROOT_FOLDER):
        if filename in files:
            return f"{root}\\{filename}"

if __name__ == "__main__":
    client_path = location_of(CLIENT_FILENAME)
    studio_path = location_of(STUDIO_FILENAME)

    try:
        run(client_path)
        print(f"Roblox launched, binary path: {client_path}")
    except CalledProcessError as err:
        print(f"Failed to launch Roblox, status code: {err.returncode} on binary: {client_path}")
    
    # Prompt to run Studio additionally, as I sometimes get into the creative spirit :3
    # ans: str = input("Would you like to run Roblox Studio additionally? ")
    print("Would you like to run Roblox Studio additionally? ")
    ans = getch().decode("utf-8")

    if ans == "y":
        # Studio should be not waited for an answer as it will not give one
        # until it has stopped, so the terminal window would remain visible
        Popen(studio_path)
        print(f"Roblox Studio should have launched. Binary path: {studio_path}")
        sleep(timeout)
    exit()
