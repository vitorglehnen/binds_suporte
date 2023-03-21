from botcity.core import DesktopBot
import pyautogui as py
import texto
import keyboard as kb
import time


class Binds(DesktopBot):
    def action(self, execution=None):
        print("Running")

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
            time.sleep(0.1)
            py.press('enter')

    def bind_stop(self, tecla):
        boolean = True

        if kb.is_pressed(tecla):
            print("Stopped")

            while boolean:
                time.sleep(0.01)
                if kb.is_pressed("ctrl+."):
                    boolean = False
                    print("Running")
                time.sleep(0.01)



Binds.main()
