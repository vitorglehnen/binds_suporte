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
    def __init__(self):
        self.loop = False

        threading.Thread(target=self.action).start()  # Inicia em outra thread o loop de binds
        self.define_icone(r'icons\icon_on.png')     # Inicia o ícone na bandeja do windows

    def action(self):
        Notification(app_id="Binds suporte", title="Running", msg="Em execução!").show()

        while not self.loop:
            time.sleep(0.05)
            self.bind()
            time.sleep(0.05)

    # Verifica se a tecla clicada se encaixa em algumas das pré definidas, caso sim, cola a frase referente
    def bind(self):
        frase = None
        if kb.is_pressed("ctrl+1"):
            frase = texto.bom_dia()
        elif kb.is_pressed("ctrl+2"):
            frase = texto.auxiliar()
        elif kb.is_pressed("ctrl+3"):
            frase = texto.algo_mais()
        elif kb.is_pressed("ctrl+4"):
            frase = texto.algo_mais()
        elif kb.is_pressed("ctrl+5"):
            frase = texto.algo_mais_simples()
        elif kb.is_pressed("ctrl+6"):
            frase = texto.fim()
        elif kb.is_pressed("ctrl+7"):
            frase = texto.ibexpert_caminho()
        elif kb.is_pressed("ctrl+8"):
            frase = texto.mk4_caminho()
        elif kb.is_pressed("ctrl+9"):
            frase = texto.impressora_caminho()
        elif kb.is_pressed("ctrl+*"):
            self.stop()

        if not frase is None:
            self.copy_paste(frase)

        time.sleep(0.01)

    # Configuração do ícone na bandeja
    def define_icone(self, image):
        self.icon = pystray.Icon('my_app_name', Image.open(image), 'Binds Suporte')
        self.icon.menu = pystray.Menu(pystray.MenuItem('Sair', self.on_exit_clicked))
        self.icon.run()

    # Define ação do programa ao clicar no botão de "Sair" no ícone da bandeja
    def on_exit_clicked(self, icon):
        icon.stop()
        self.loop = True
        return self.loop

    # Função para dar um stop no programa, não deixando fazer nenhuma ação
    def stop(self):
        ativo = True

        Notification(app_id="Binds suporte", title="Stopped", msg="Serviço parado!").show()

        # Alterna ícone da bandeja para a luz desligada, demonstrando que o programa está parado
        self.icon.icon = Image.open(r'icons\icon_off.png')
        time.sleep(0.1)

    # Após parar o programa, fica nesse loop, que espera a tecla de stop ser clicada novamente para voltar a execução
        while ativo:
            time.sleep(0.1)
            if kb.is_pressed("ctrl+*"):
                Notification(app_id="Binds suporte", title="Running", msg="Em execução!").show()
                self.icon.icon = Image.open(r'icons\icon_on.png')
                ativo = False
            time.sleep(0.1)

    def copy_paste(self, str):
        pyperclip.copy(str)
        py.hotkey('ctrl', 'v')


Binds()
