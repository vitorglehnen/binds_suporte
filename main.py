from botcity.core import DesktopBot
import texto
import keyboard as kb
import time


class Binds(DesktopBot):
    def action(self, execution=None):
        print("Running")

        while True:
            time.sleep(0.01)
            self.bind("ctrl+1", texto.bom_dia())
            self.bind("ctrl+2", texto.fim())
            self.bind("ctrl+3", texto.remoto())
            self.bind("ctrl+4", texto.algo_mais())
            time.sleep(0.01)

    def bind(self, tecla, texto):
        if kb.is_pressed(tecla):
            self.paste(texto)


Binds.main()
