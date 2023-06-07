import tkinter as tk
from tkinter import *
import pyperclip as pc


class Form:
    def __init__(self):
        self.binds = open('binds.txt', 'r')
        self.janela = tk.Tk()
        self.janela.title('teste')
        self.janela.geometry('250x600')
        x = self.janela.winfo_pointerx()
        y = self.janela.winfo_pointery()
        self.janela.geometry(f"+{x}+{y}")

        for bind in self.binds:
            Button(self.janela, text=bind, command=lambda txt=bind.strip(): self.atribue_clipboard(txt)).pack(
                anchor=tk.N, fill=tk.X)

        self.janela.mainloop()

    def atribue_clipboard(self, texto):
        pc.copy(texto)
        self.janela.destroy()

