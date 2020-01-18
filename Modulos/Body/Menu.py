from time import sleep
import os, glob
def menu():
        print("""
        __   __          ____
        \ \ / /__  _   _|  _ \  _____      __
         \ V / _ \| | | | | | |/ _ \ \ /\ / /
          | | (_) | |_| | |_| | (_) \ V  V /
          |_|\___/ \__,_|____/ \___/ \_/\_/
                <==================>
                   [1] Videos
                   [2] Musica
                   [3] PlayList
                   [4] Lista Tudo
                   [5] Sair
                <==================>
        """)
def loop():
    loop = 0
    while loop != 4:
        os.system("clear")
        print("Iniciando", end="")
        print(".")
        sleep (0.3)
        os.system("clear")
        print("Iniciando", end="")
        print("..")
        sleep (0.3)
        os.system("clear")
        print("Iniciando", end="")
        print("...")
        sleep (0.3)
        os.system("clear")
        loop = loop + 1

def baixa():
    baixa = 0
    while baixa != 5:
        os.system("clear")
        print("Iniciando Downloads", end="")
        print(".")
        sleep (0.3)
        os.system("clear")
        print("Iniciando Downloads", end="")
        print("..")
        sleep (0.3)
        os.system("clear")
        print("Iniciando Downloads", end="")
        print("...")
        sleep (0.3)
        os.system("clear")
        print("Aguardem...")
        baixa = baixa + 1
def lista():
    os.chdir("/data/data/com.termux/files/home/YouDow")
    a = glob.glob("*.mp3")
    b = glob.glob("*.webm")
    c = glob.glob("*.mkv")
    print("                 LISTA DE DOWNLOADS")
    print("===========================================================")
    for ar1 in a:
        print(ar1)
    for ar2 in b:
        print(ar2)
    for ar3 in c:
        print(ar3)
    print("===========================================================")
