import tkinter.messagebox as tm
import os
import tkinter.simpledialog as ts
from tkinter import *
from tkinter.filedialog import *

def cTof():
    c = float(entry1.get())
    f = 9/5*c + 32
    entry2.delete(0, END)
    entry2.insert(0, str(f))

def fToc():
    f = float(entry2.get())
    c = 5/9*(f-32)
    entry1.delete(0, END)
    entry1.insert(0, str(c))

def temperature():
    global entry1, entry2

    window = Tk()
    window.title("온도 변환 프로그램")
    window.geometry('250x150')

    label1 = Label(window, text="온도 변환 프로그램")
    label2 = Label(window, text="섭씨")
    label3 = Label(window, text="화씨")
    label1.grid(row = 0, column = 0, columnspan = 2)
    label2.grid(row = 1, column = 0)
    label3.grid(row = 2, column = 0)

    entry1 = Entry(window)
    entry2 = Entry(window)

    entry1.grid(row = 1, column = 1)
    entry2.grid(row = 2, column = 1)

    btn1 = Button(window, text = "섭씨 -> 화씨", command = cTof)
    btn2 = Button(window, text = "화씨 -> 섭씨", command = fToc)

    btn1.grid(row = 3, column = 0)
    btn2.grid(row = 3, column = 1)

    window.mainloop()