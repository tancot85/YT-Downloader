#app.py
import tkinter as tk
from functools import partial
from tkinter import *
import main as downloader

master= tk.Tk()
streams = []

def logic(video):
    streams = get_all_strems(video)

tk.Label(master, text="Enter Url").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

def print_something(something):
    downloader.download_stream(something)
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(root, yscrollcommand = scrollbar.set )
    for line in range(len(streams)):
       mylist.insert(END,str(line)+str(streams[line]))
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
B = Button(master, text ="Hello", command = partial(print_something,e1.get())).grid(row=1,columnspan=2)
master.mainloop()
