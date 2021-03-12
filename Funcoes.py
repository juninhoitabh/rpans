import pyautogui as p
# import rpa as r
# import smtplib
# import Emails as e
import datetime as d


def logaSistema(sistema, operador, senha):  # Abre o sistema e faz Login
    caminho = 'C:\\Program Files (x86)\\Teknisa Web\\Bin\\Client\\' + str(sistema) + '.exe'
    # print(caminho)
    p.hotkey('win', 'r')
    p.sleep(1)
    p.typewrite(caminho)
    p.press('enter')
    p.sleep(4)
    p.typewrite('9999')
    p.press('tab')
    p.typewrite(str(operador))
    p.press('tab')
    p.typewrite(str(senha))
    p.press('enter')
    p.sleep(12)
    p.press('enter')
    p.sleep(3)
    return ()


def posicaoMenu(numero):  # Retorna as coordenadas dos itens no menu de acordo com a posição
    vertical = 32
    horizontal = 0
    if numero == 1:
        horizontal = 12
    else:
        if numero == 2:
            horizontal = 130
        if numero == 3:
            horizontal = 170
        if numero == 4:
            horizontal = 300
        if numero == 5:
            horizontal = 380
    return horizontal, vertical


def posicaoSubmenu(menu, submenu):  # Retorna as coordenadas do item no submenu em relação ao menu informado

    vertical = 25 + (submenu * 20)  # 20 é a distancia entre os itens no submenu
    # print(vertical
    horizontal, verticalMenu = posicaoMenu(menu)
    return horizontal, vertical

#encerra o módulo do Sistema
def fecharModulo(modulo):
    p.hotkey('win','r')
    p.typewrite('taskkill /f /fi "imagename eq '+str(modulo)+'.exe"')
    p.press('enter')


#Retorna uma string com o dia e a hora sem caracteres especiais
def dataHora():
    nome = str(d.datetime.now().day)+'-'+str(d.datetime.now().month)+'-'+str(d.datetime.now().year)+'-'
    nome = nome + str(d.datetime.now().hour)+str(d.datetime.now().minute)+str(d.datetime.now().second)
    return (nome)
# p.sleep(2)
# print(p.position())
