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


def calculaNecessidadeCompra(filial, data_inicial, data_final, produto_inicial, produto_final, acrescimo):
    # Navega até o item Cálculo de necessidade de compras
    p.click(posicaoMenu(1))
    p.moveTo(posicaoSubmenu(1, 2))
    (p.sleep(1))
    p.click(posicaoSubmenu(4, 2))
    (p.sleep(2))
    # preenche o formulário
    p.click(x=785, y=473)
    p.click(x=851, y=474)
    p.sleep(1)
    p.click(x=952, y=441)
    p.sleep(1)
    p.click(x=874, y=437)
    p.press('c')
    p.click(x=952, y=441)
    p.press('tab')
    p.typewrite(filial)
    p.sleep(1)
    p.doubleClick(x=981, y=506)
    p.press('enter')
    p.press('tab')
    p.typewrite(data_inicial)
    p.press('tab')
    p.typewrite(data_final)
    p.press('tab')
    p.press('tab')
    p.typewrite(produto_inicial)
    p.press('tab')
    p.typewrite(produto_final)
    p.press('tab')
    if produto_final == '114':
        acrescimo = '3'
    p.typewrite(acrescimo)
    p.press('tab')
    p.press('space')


def calculaPrevia(filial, data_inicial, data_final, produto_inicial, produto_final, acrescimo):

    # Navega até o item Cálculo de necessidade de compras
    p.click(posicaoMenu(1))
    p.click(posicaoSubmenu(1, 1))
    (p.sleep(2))

    # preenche o formulário
    p.click(x=932, y=468)
    p.sleep(1)
    p.click(x=929, y=472)
    p.sleep(1)
    p.click(x=999, y=472)
    p.sleep(1)
    p.click(x=952, y=441)
    p.press('c')
    p.click(x=952, y=441)
    p.press('tab')
    p.typewrite(filial)
    p.sleep(1)
    p.doubleClick(x=981, y=506)
    p.press('enter')
    p.sleep(1)
    p.press('tab')
    p.typewrite(data_inicial)
    p.press('tab')
    p.typewrite(data_final)
    p.press('tab')
    p.press('tab')
    if produto_final == '114':
        acrescimo = '3'
    p.typewrite(acrescimo)
    p.press('tab')
    p.press('space')
    p.press('tab')
    p.press('tab')
    p.typewrite(produto_inicial)
    p.press('tab')
    p.typewrite(produto_final)
    p.press('tab')
    # p.press('tab')
    # p.click(x=879, y=370)
    # p.sleep(3)
    p.click(x=788, y=362)
    p.sleep(1)
    p.click(x=861, y=528)
    p.sleep(1)
    p.typewrite('c:\APC')
    p.press('enter')
    p.typewrite('Previa' + filial + ' - ' + dataHora())
    p.press('enter')
    p.sleep(15)
    p.click(x=952, y=441)
    p.sleep(1)
    p.press('enter')

def calculaPreviaNecessidade(filial, data_inicial, data_final, produto_inicial, produto_final, acrescimo):
    p.click(posicaoMenu(1))
    p.moveTo(posicaoSubmenu(1, 2))
    (p.sleep(1))
    p.click(posicaoSubmenu(4, 4))
    (p.sleep(2))
    p.press('tab')
    p.typewrite(filial)
    p.press('tab')
    p.typewrite(data_inicial)
    p.press('tab')
    p.typewrite(data_final)
    p.press('tab')
    p.press('tab')
    p.typewrite(produto_inicial)
    p.press('tab')
    p.typewrite(produto_final)
    p.press('tab')
    if produto_final == '114':
        acrescimo = '3'
    p.typewrite(acrescimo)
    p.click(x=813, y=397)
    (p.sleep(1))
    p.click(x=913, y=563)
    p.sleep(1)
    p.typewrite('c:\APC')
    p.press('enter')
    p.typewrite('Previa calculo necessidade -' + filial + ' - ' + f.dataHora())
    p.press('enter')
    p.sleep(15)
    p.click(x=952, y=441)
    p.sleep(1)
    p.press('enter')
p.sleep(3)
print(p.position())
