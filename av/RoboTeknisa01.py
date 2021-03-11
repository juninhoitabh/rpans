import pyautogui as p
import rpa as r
import Funcoes as f

f.LogaSistema('dfe','1027','123658')
p.click(f.PosicaoMenu(1))
p.sleep(2)
p.moveTo(f.PosicaoSubmenu(1,5))
p.sleep(2)
p.click(f.PosicaoSubmenu(1,5))
p.sleep(2)
p.typewrite('03')
p.press('tab')
p.sleep(1)
