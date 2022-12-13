import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

FOOTER = 5

class Editor:
    def __init__(self, mainwindow,name, rows, coloum):
        if name is not None:self.name = name
        self.mainwindow = mainwindow
        self.rows = rows
        self.coloum = coloum
        self.editwin = curses.newwin(self.rows-self.rows//5, self.coloum-2, 1, 1)
        self.box = Textbox(self.editwin)
    def run(self):
        while True:
            self.box.edit()
            self.editwin.refresh()
            self.mainwindow.refresh()



def main(stdscr):
    rows, cols = stdscr.getmaxyx()
    edit = Editor(stdscr,None,rows, cols)
    edit.run()

wrapper(main)
