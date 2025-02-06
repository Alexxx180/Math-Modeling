from msvcrt import kbhit, getch

def win_clear():
    while kbhit():
        getch()
    return 'cls'
