from winotify import Notification
import pyautogui as py
import keyboard as kb
from PIL import Image
import threading
import pyperclip
import pystray
import texto
import time


class Binds:
    loop = False

    def __init__(self):
        threading.Thread(target=self.action).start()
        self.define_icone(r'icons\icon_on.png')

    def on_exit_clicked(self, icon):
        icon.stop()
        self.loop = True
        return self.loop

    def define_icone(self, image):
        self.icon = pystray.Icon('my_app_name', Image.open(image), 'Binds Suporte')
        self.icon.menu = pystray.Menu(pystray.MenuItem('Exit', self.on_exit_clicked))
        self.icon.run()

    def action(self):
        toast = Notification(app_id="Binds suporte", title="Running", msg="Em execução!")
        toast.show()

        while not self.loop:
            time.sleep(0.05)
            self.bind("ctrl+1", texto.bom_dia())
            self.bind("ctrl+2", texto.auxiliar())
            self.bind("ctrl+3", texto.acesso())
            self.bind("ctrl+4", texto.algo_mais())
            self.bind("ctrl+5", texto.algo_mais_simples())
            self.bind("ctrl+6", texto.fim())
            self.bind_win("ctrl+7", texto.ibexpert_caminho())
            self.bind_win("ctrl+8", texto.mk4_caminho())
            self.bind_win("ctrl+9", texto.impressora_caminho())
            self.bind_stop("ctrl+*")
            time.sleep(0.05)

    def bind(self, tecla, frase):
        if kb.is_pressed(tecla):
            self.copia_cola(frase)

    def bind_win(self, tecla, caminho):
        if kb.is_pressed(tecla):
            self.copia_cola(caminho)
            time.sleep(0.8)
            py.press('enter')

    def bind_stop(self, tecla):
        boolean = True

        if kb.is_pressed(tecla):
            toast = Notification(app_id="Binds suporte", title="Stopped", msg="Serviço parado!")
            print("Stopped")
            toast.show()
            self.icon.icon = Image.open(r'icons\icon_off.png')

            while boolean:
                time.sleep(0.05)
                if kb.is_pressed("ctrl+0"):
                    toast = Notification(app_id="Binds suporte", title="Running", msg="Em execução!")
                    toast.show()
                    print("Running")
                    self.icon.icon = Image.open(r'icons\icon_on.png')
                    boolean = False
                time.sleep(0.05)

    def copia_cola(self, str):
        pyperclip.copy(str)
        py.hotkey('ctrl', 'v')


Binds()
