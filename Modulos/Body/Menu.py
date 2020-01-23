import random
from time import sleep
import os, glob
def menu():
        print("""		<===============================>
	                   [1] Videos
	                   [2] Musica
	                   [3] PlayList
	                   [4] Lista Tudo
	                   [5] Sair
                <===============================>
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
def listaM():
    os.chdir("/data/data/com.termux/files/home/storage/shared/Music")
    a = glob.glob("*.mp3")
    b = glob.glob("*.webm")
    c = glob.glob("*.mkv")
    d = glob.glob("*.mp4")
    print("                 LISTA DE MUSICA (Music)")
    print("===========================================================")
    for ar1 in a:
        print(ar1)
    for ar2 in b:
        print(ar2)
    print("===========================================================")
def listaV():
    os.chdir("/data/data/com.termux/files/home/storage/shared/Movies")
    c = glob.glob("*.mkv")
    d = glob.glob("*.mp4")
    print("                 LISTA DE VIDEOS (Movies)")
    print("===========================================================")
    for ar3 in c:
        print(ar3)
    for ar4 in d:
        print(ar4)
    print("===========================================================")
def logo1():
    os.system("figlet -c YouDow")
def logo2():
    os.system("figlet -c -f banner YouDow")
def logo3():
    os.system("figlet -c -f slant YouDow")
def logo4():
    os.system("figlet -c -f small YouDow")
def logo5():
    os.system("figlet -c -f smslant YouDow")

lo1 = logo1
lo2 = logo2
lo3 = logo3
lo4 = logo4
lo5 = logo5
logos = [lo1, lo2, lo3, lo4, lo5]
escolha = random.choice(logos)
