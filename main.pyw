from winotify import Notification
import pyautogui as py
import keyboard as kb
from PIL import Image
import threading
import pyperclip
import pystray
import texto
import time

loop = False


def on_exit_clicked(icon):
    global loop
    icon.stop()
    loop = True
    return loop


def icone_bandeja():
    icon = pystray.Icon('my_app_name', Image.open(r'C:\Users\vitor.lehnen\Desktop\binds_suporte\ideia.png'),
                        'Binds '
                        'Suporte')

    icon.menu = pystray.Menu(
        pystray.MenuItem('Exit', on_exit_clicked))

    icon.run()


def action():
    global loop
    toast = Notification(app_id="Binds suporte",
                         title="Running",
                         msg="Em execução!")
    toast.show()

    while not loop:
        time.sleep(0.01)
        bind("ctrl+1", texto.bom_dia())
        bind("ctrl+2", texto.auxiliar())
        bind("ctrl+3", texto.acesso())
        bind("ctrl+4", texto.algo_mais())
        bind("ctrl+5", texto.algo_mais_simples())
        bind("ctrl+6", texto.fim())
        bind_win("ctrl+7", texto.ibexpert_caminho())
        bind_win("ctrl+8", texto.mk4_caminho())
        bind_win("ctrl+9", texto.impressora_caminho())
        bind_stop("ctrl+*")
        time.sleep(0.01)


def bind(tecla, frase):
    if kb.is_pressed(tecla):
        copia_cola(frase)


def bind_win(tecla, caminho):
    if kb.is_pressed(tecla):
        copia_cola(caminho)
        time.sleep(0.8)
        py.press('enter')


def bind_stop(tecla):
    boolean = True

    if kb.is_pressed(tecla):
        print("Stopped")
        toast = Notification(app_id="Binds suporte",
                             title="Stopped",
                             msg="Serviço parado!")
        toast.show()

        while boolean:
            time.sleep(0.01)
            if kb.is_pressed("ctrl+*"):
                boolean = False
                toast = Notification(app_id="Binds suporte",
                                     title="Running",
                                     msg="Em execução!")
                toast.show()
            time.sleep(0.01)


def copia_cola(str):
    pyperclip.copy(str)
    py.hotkey('ctrl', 'v')


t = threading.Thread(target=action)
t.start()

icone_bandeja()
