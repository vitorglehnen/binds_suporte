from datetime import time as tm, date, datetime
import pyautogui as py


def fim():
    data_hoje = datetime.today()

    if data_hoje.weekday() > 3:
        complemento = "um bom fim de semana!"
    else:
        complemento = "um bom dia!"

    texto = f"Certo, qualquer coisa só retornar, tenha um ótimo trabalho e {complemento}"
    return texto


def algo_mais():
    texto = "Pronto, posso te auxiliar em mais alguma coisa?"
    return texto


def bom_dia():
    hora_agora = datetime.now().time()

    if hora_agora > tm(12, 0, 0):
        saudacao = "Boa tarde"
    else:
        saudacao = "Bom dia"

    texto = f"{saudacao}, sou o Vitor, estou aqui para te auxiliar 😁"
    return texto


def acesso():
    texto = 'Consegue me passar o acesso da máquina para verificar? Pode ser AnyDesk, TeamViewer, Acesso Remoto... '
    return texto


def auxiliar():
    texto = 'Em que posso te ajudar?'
    return texto


def algo_mais_simples():
    texto = 'Posso auxiliar em mais alguma coisa?'
    return texto


def ibexpert_caminho():
    caminho = r'\Sistema\MK4\Uteis\ibexpert\ibexpert.exe'
    return caminho

def mk4_caminho():
    caminho = r'\Sistema\MK4\MKeyAtu.exe'
    return caminho

def impressora_caminho():
    caminho = r'control printers'
    return caminho
