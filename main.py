from winotify import Notification
import keyboard as kb
from PIL import Image as img
import threading
import pystray
import time
import tkinter as tk
from tkinter import *
import pyperclip as pc


class Binds:
    def __init__(self):
        self.loop = False

        threading.Thread(target=self.action).start()
        self.define_icone(r'icons\icon_on.png')


    def action(self):
        Notification(app_id="Binds suporte", title="Running", msg="Em execução!").show()

        while not self.loop:
            time.sleep(0.01)
            self.bind()
            time.sleep(0.01)


    def bind(self):
        if kb.is_pressed("ctrl+1"):
            self.frase = Form()

        time.sleep(0.01)


    def define_icone(self, image):
        self.icon = pystray.Icon('my_app_name', img.open(image), 'Binds Suporte')
        self.icon.menu = pystray.Menu(pystray.MenuItem('Sair', self.on_exit_clicked))
        self.icon.run()


    def on_exit_clicked(self, icon):
        icon.stop()
        self.loop = True
        return self.loop


class Form:
    def __init__(self):
        self.binds = open('binds.txt', 'r', encoding='utf-8')
        self.janela = tk.Tk()
        self.janela.title('Binds')
        self.janela.geometry('600x600')
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


Binds()
