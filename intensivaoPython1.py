import pyautogui
import pyperclip
import time
import pandas as pd
import os
import datetime as dt

time.sleep(5)
print(pyautogui.position())

pyautogui.PAUSE = 1

pyautogui.press("win")  # Pressiona a telca windows
pyautogui.write("brave")  # Digita brave no windows
pyautogui.press("enter")  # Pressiona enter parar abrir o navegador

# pyautogui.hotkey("ctrl", "shift", "n")
pyautogui.write(
    "https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")  # Digita o link no navegador
pyautogui.press("enter")  # Pressiona a tecla enter para entrar no site do link

time.sleep(3)

pyautogui.click(x=3252, y=435)
pyautogui.write("meu_login")  # Digita usuario

pyautogui.click(x=3252, y=510)
pyautogui.write("minha_senha")

pyautogui.click(x=3252, y=590)
time.sleep(3)

pyautogui.click(x=3075, y=371)
pyautogui.click(x=3155, y=860)
time.sleep(3)
pyautogui.press("enter")
time.sleep(6)

tabela = pd.read_csv(r"S:\Downloads\Compras.csv", sep=";")
# print(tabela)

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade
print(
    f"Total Gasto: {total_gasto}\nQuantidade: {quantidade}\nPreço Médio: {preco_medio}")

os.remove(r"S:\Downloads\Compras.csv")

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/2/#inbox")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=2647, y=264)
pyautogui.write("gustavohenrique9165@gmail.com")
pyautogui.press("enter")
pyautogui.press("tab")

# texto com pontuação e ja copia
pyperclip.copy(f"Relatório Analítico de Compras {dt.date.today()}")
pyautogui.hotkey("ctrl", "v")  # cola o texto com pontuação
pyautogui.press("tab")

texto = f"""
Prezados,
Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f} 
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, é só falar.
Att., Gustavo Rocha
"""
pyperclip.copy(texto)  # texto com pontuação e ja copia
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")  # enviar email

print("Deu tudo certo!")

#  pyautogui.click -> clique com o mouse
#  pyautogui.write -> escrever um texto
#  pyautogui.press $ -> apertar uma tecla
#  pyautogui.hotkey -> apertar uma combinação de teclas (ex: Ctrl + D)
