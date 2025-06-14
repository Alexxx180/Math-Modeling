import platform
from os import system
from msvcrt import kbhit, getch

def win_clear():
	while kbhit(): getch()
	return 'cls'

def clear():
	windows = platform.system() == "Windows" 
	system(win_clear() if windows else 'clear')
