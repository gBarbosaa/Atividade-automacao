import pyautogui
import time

"""#Pausa geral de 0.3 segundos (300 milissegundos)
pyautogui.PAUSE = 0.3

#ESPERA  UM TEMPO PRA RODAR
time.sleep(2)

#Pegar posição do mouse
#print(pyautogui.position())

#Pegar tamanho da tela
#print(pyautogui.size())

#pyautogui.click(x=233, y=365)

#clicar botao direito
#pyautogui.click(x=233, y=365, button= right)
pyautogui.click(x=233, y=365)

#miver o mouse
pyautogui.moveTo(x=720, y=225, duration=1)
pyautogui.moveTo(x=670, y=310, duration=1)
pyautogui.moveTo(x=865, y=320, duration=1)
pyautogui.click(x= 865, y=320)
#rloar pagina num- scroll pra baixo
pyautogui.scroll(-850)
pyautogui.click(x= 868, y=475)
pyautogui.moveTo(x=1344, y=217, duration=2)
"""

# print(pyautogui.KEYBOARD_KEYS)

pyautogui.press("win")

pyautogui.write("Clima")

pyautogui.press("enter", )