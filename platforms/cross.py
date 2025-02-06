import platform
from os import system
from platforms.windows import win_clear

def clear():
    windows = platform.system() == "Windows" 
    system(win_clear() if windows else 'clear')
