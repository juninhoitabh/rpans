import rpa as r
import pyautogui as p

r.init()
r.url('https://helpdesk.nsabor.com.br')
r.wait(3.0)
janela = p.getActiveWindow()
janela.maximize()
r.type('login_name','suporte')
r.type('login_password','57xzaw15',rpa,en)

