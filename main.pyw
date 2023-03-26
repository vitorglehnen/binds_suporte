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
            self.bind()
            self.bind_stop("ctrl+*")
            time.sleep(0.05)

    def bind(self):
        if kb.is_pressed("ctrl+1"):
            self.copia_cola(texto.bom_dia())
        elif kb.is_pressed("ctrl+2"):
            self.copia_cola(texto.auxiliar())
        elif kb.is_pressed("ctrl+3"):
            self.copia_cola(texto.acesso())
        elif kb.is_pressed("ctrl+4"):
            self.copia_cola(texto.algo_mais())
        elif kb.is_pressed("ctrl+5"):
            self.copia_cola(texto.algo_mais_simples())
        elif kb.is_pressed("ctrl+6"):
            self.copia_cola(texto.fim())
        elif kb.is_pressed("ctrl+7"):
            self.copia_cola(texto.ibexpert_caminho())
        elif kb.is_pressed("ctrl+8"):
            self.copia_cola(texto.mk4_caminho())
        elif kb.is_pressed("ctrl+9"):
            self.copia_cola(texto.impressora_caminho())

        time.sleep(0.01)

    def bind_stop(self, tecla):
        boolean = True

        if kb.is_pressed(tecla):
            toast = Notification(app_id="Binds suporte", title="Stopped", msg="Serviço parado!")
            print("Stopped")
            toast.show()
            self.icon.icon = Image.open(r'icons\icon_off.png')
            time.sleep(0.1)

            while boolean:
                time.sleep(0.1)
                if kb.is_pressed("ctrl+*"):
                    toast = Notification(app_id="Binds suporte", title="Running", msg="Em execução!")
                    toast.show()
                    print("Running")
                    self.icon.icon = Image.open(r'icons\icon_on.png')
                    boolean = False
                time.sleep(0.1)

    def copia_cola(self, str):
        pyperclip.copy(str)
        py.hotkey('ctrl', 'v')


Binds()
