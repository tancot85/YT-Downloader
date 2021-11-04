import tkinter as tk
from functools import partial
from tkinter import *
import main as downloader

master= tk.Tk()

tk.Label(master, text="Enter Url").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

def print_something(something):
    downloader.download_stream(something)
B = Button(master, text ="Hello", command = partial(print_something,e1.get())).grid(row=1,columnspan=2)
master.mainloop()
