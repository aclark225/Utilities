# will find each unique item/word in a list 
# supports delimiters

import os, sys, re
import tkinter as tk
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def find_unique(delimiter, file_name):

    find_unique_win = tk.Tk()
    
    find_unique_win.mainloop()
    

def text_editor():
    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        text_window.title(f"Text Editor Application - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        # filepath = asksaveasfilename(
            # defaultextension="txt",
            # filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        # )
        
        filepath = "T_E_M_P.txt"
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        text_window.destroy()
        #text_window.title(f"Text Editor Application - {filepath}")

    text_window = tk.Tk()
    text_window.title("Text Editor Application")
    text_window.rowconfigure(0, minsize=300, weight=1)
    text_window.columnconfigure(1, minsize=300, weight=1)

    txt_edit = tk.Text(text_window)
    fr_buttons = tk.Frame(text_window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    text_window.mainloop()
