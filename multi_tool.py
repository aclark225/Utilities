import sys, os
import tkinter as tk
from tkinter import ttk
from functions.find_uniques import *

window = tk.Tk()
window.title("Multi-Tool")
window.geometry("300x300")

def init_find_uniques():

    text_editor()
    find_unique(',', "text.txt")
    
def main():
    
    btn_find = ttk.Button(window, text="Find Uniques", command=init_find_uniques)
    
    btn_find.place(x=10, y=10)
    
    window.mainloop()
    
main()