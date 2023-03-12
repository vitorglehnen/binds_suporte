from datetime import time as tm, date, datetime
from botcity.core import DesktopBot
import keyboard as kb
import time



class Binds(DesktopBot):
    def action(self, execution=None):
        print("Running")
        while True:
            time.sleep(0.01)
            if kb.is_pressed("ctrl+1"):
                self.paste(self.bom_dia())
            elif kb.is_pressed("ctrl+2"):
                self.paste(self.fim())
            elif kb.is_pressed("ctrl+3"):
                self.paste(self.algo_mais())
            elif kb.is_pressed("ctrl+4"):
                self.paste(self.remoto())
            time.sleep(0.01)

    def fim(self):
        data_hoje = datetime.today()

        if data_hoje.weekday() > 3:
            complemento = "um bom fim de semana!"
        else:
            complemento = "um bom dia!"

        texto = f"Certo, qualquer coisa só retornar, tenha um ótimo trabalho e {complemento}"
        return texto

    def algo_mais(self):
        texto = "Pronto, posso te auxiliar em mais alguma coisa?"
        return texto

    def bom_dia(self):
        hora_agora = datetime.now().time()

        if hora_agora > tm(12, 0, 0):
            saudacao = "Boa tarde"
        else:
            saudacao = "Bom dia"

        texto = f"{saudacao} , sou o Vitor, estou aqui para te auxiliar 😁"
        return texto

    def remoto(self):
        texto = 'Consegue me passar o acesso da máquina para verificar? Pode ser AnyDesk, TeamViewer, Acesso Remoto... '
        return texto


Binds.main()
