import sys
from botcity.core import DesktopBot
from winotify import Notification
from PIL import Image
import pystray
import pyautogui as py
import texto
import keyboard as kb
import time


class Binds(DesktopBot):

    async def action(self, execution=None):
        toast = Notification(app_id="Binds suporte",
                             title="Running",
                             msg="Em execução!")
        toast.show()
        

        while True:
            time.sleep(0.01)
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
            time.sleep(0.01)

    def bind(self, tecla, texto):
        if kb.is_pressed(tecla):
            self.paste(texto)

    def bind_win(self, tecla, caminho):
        if kb.is_pressed(tecla):
            self.paste(caminho)
            time.sleep(0.8)
            py.press('enter')

    def bind_stop(self, tecla):
        boolean = True

        if kb.is_pressed(tecla):
            print("Stopped")
            toast = Notification(app_id="Binds suporte",
                                 title="Stopped",
                                 msg="Serviço parado!")
            toast.show()

            while boolean:
                time.sleep(0.01)
                if kb.is_pressed("ctrl+."):
                    boolean = False
                    toast = Notification(app_id="Binds suporte",
                                         title="Running",
                                         msg="Em execução!")
                    toast.show()
                time.sleep(0.01)

    def on_exit_clicked(self, icon):
        icon.stop()
        sys.exit()

    async def icone_bandeja(self):
        icon = pystray.Icon('my_app_name', Image.open('ideia.png'))
        icon.menu = pystray.Menu(
            pystray.MenuItem('Exit', self.on_exit_clicked)
        )

        icon.run()


Binds.main()
