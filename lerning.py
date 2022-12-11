import curses
from curses import wrapper
import time

WELCOME_TEXT = "Welcome to my Terminal-Based-Text-Editor"
FUNCTION_LIST = ["pass","pass","pass"]

#addstr - postiony,postionx,text,attributes
#init_pair(farb sets) - channel,foreground color, backgroundcolor
#stdscr.addstr(10,10,"Hello, World!",curses.color_pair(1) | curses.A_UNDERLINE)


def menu(stdscr):
    rows, cols = stdscr.getmaxyx()
    center_y, center_x = rows // 2, cols // 2
    #first two rows
    stdscr.addstr(0,center_x-(len(WELCOME_TEXT)//2),WELCOME_TEXT,curses.A_UNDERLINE | curses.A_BOLD)
    stdscr.addstr(2,center_x-(len("Select something, press enter for select and < - > for navigate")//2),"Select something, press enter for select and < - > for navigate")
    #creating the function seletction menu
    for i in range(len(FUNCTION_LIST)):
        seqments = cols//(1+len(FUNCTION_LIST))
        #caculating the perfect middle for each text selection
        x = seqments*(i+1)-(len(FUNCTION_LIST)//2)
        stdscr.addstr(4,x,FUNCTION_LIST[i])
    
    #selection module
    selected = 0
    while (key := stdscr.getch()) != 113:
        seqments = cols//(1+len(FUNCTION_LIST))
        if key == 260:#links
            #setting selected befor back to normal
            stdscr.addstr(4,x,FUNCTION_LIST[selected % len(FUNCTION_LIST)])
            
            selected = selected - 1
            
            #calculate postionx
            x = seqments*(selected % len(FUNCTION_LIST) + 1)-(len(FUNCTION_LIST)//2)
            #marker the new selected
            stdscr.addstr(4,x,FUNCTION_LIST[selected % len(FUNCTION_LIST)],curses.A_REVERSE)
        if key == 261:#rechts
            #setting selected befor back to normal
            stdscr.addstr(4,x,FUNCTION_LIST[selected % len(FUNCTION_LIST)])
            
            selected = selected + 1
            
            #calculate postionx
            x = seqments*(selected % len(FUNCTION_LIST) + 1)-(len(FUNCTION_LIST)//2)
            #marker the new selected
            stdscr.addstr(4,x,FUNCTION_LIST[selected % len(FUNCTION_LIST)],curses.A_REVERSE)
        stdscr.refresh()
    print(key)




wrapper(menu)

