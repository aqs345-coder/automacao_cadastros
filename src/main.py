import time

import pandas
import pyautogui
from utils import LINK, TABLE_PATH

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("opera GX")
pyautogui.press("enter")
pyautogui.write(LINK)
pyautogui.press("enter")

time.sleep(1)

pyautogui.press("tab")
pyautogui.write("emaildeexemplo@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

table = pandas.read_csv(TABLE_PATH)

pyautogui.PAUSE = 0.01
for linha in table.index:
    time.sleep(0.3)
    pyautogui.click(x=1288, y=241)

    codigo = table.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = table.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = table.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = table.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = table.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = table.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = table.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")
