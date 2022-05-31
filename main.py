# Tic-Tac-Toe game

from time import sleep
import curses
from os import system

def winner(b, turn):
    players = ("Player 1", "Player 2")
    for i in range(3):
        if (b[i*3] == b[i*3+1] == b[i*3+2] != " " or
            b[i]   == b[i+3]   == b[i+6]   != " "   ):
            return f"{players[turn%2]} wins!"
    if (b[0] == b[4] == b[8] != " " or
        b[2] == b[4] == b[6] != " " ):
        return f"{players[turn%2]} wins!"
    return "No winner"

def main(stdscr):
    y,x = stdscr.getmaxyx()
    y = y//2-3
    x = x//2-5
    curses.curs_set(0)
    curses.mousemask(1)
    board = lambda b: "╔═══╦═══╦═══╗\n║ {} ║ {} ║ {} ║\n╠═══╬═══╬═══╣\n║ {} ║ {} ║ {} ║\n╠═══╬═══╬═══╣\n║ {} ║ {} ║ {} ║\n╚═══╩═══╩═══╝".format(*b)
    b = list(" "*9)
    xs = [2,6,10]
    ys = [1,3,5]
    #print(board(b1))
    #sleep(1)
    #print(board(b2))
    for i,r in enumerate(board(b).split("\n")):
        stdscr.addstr(y+i, x, r)
    turn = 0
    symbols = "XO" 
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    while True:    
        key = stdscr.getch()
        if key == curses.KEY_MOUSE:
            _, mx, my, *_ = curses.getmouse()
            rx, ry = mx-x, my-y
            if rx in xs and ry in ys:
                ix, iy = xs.index(rx), ys.index(ry)
                if b[iy*3+ix] == " ": 
                    b[iy*3+ix] = symbols[turn%2]
                else: continue
            else: continue
            for i,r in enumerate(board(b).split("\n")):
                stdscr.addstr(y+i, x, r)
            stdscr.addstr(my, mx, symbols[turn%2], curses.color_pair(turn%2+1))
            w = winner(b, turn)
            if w != "No winner":
                for i,r in enumerate(board(b).split("\n")):
                    stdscr.addstr(y+i, x, r)
                stdscr.addstr(y+7, x-1, w)
                stdscr.refresh()
                sleep(3)
                quit()
            if " " not in b: 
                stdscr.addstr(y+7, x, w)
                stdscr.refresh()
                sleep(2)
                quit()
            turn += 1
curses.wrapper(main)


