from tkinter import *
from tkinter.filedialog import *

def click(key):
    if key == '=': display.insert(END, '=' + str(eval(display.get())))
    elif key == 'C': display.delete(0, END)
    elif key == '←': display.delete(len(display.get()) -1, END)
    else: display.insert(END, key)

def calcMain():
    global display
    window = Tk()
    window.title('My caculator')
    display = Entry(window, width = 50, bg = 'yellow')
    display.grid(row = 0, column = 0, columnspan = 5)

    button_list = '7,8,9,/,C,4,5,6,*,%,1,2,3,-,**,0,.,=,+,←'.split(',')
    row_index = 1

    for button_text in button_list:
        col_index = button_list.index(button_text)
        if col_index % 5 == 0: row_index += 1
        btn = Button(window, text=button_text, width = 9, height = 2\
                    ,command = lambda x = button_text : click(x))\
                    .grid(row = row_index, column = col_index % 5)

    window.mainloop()