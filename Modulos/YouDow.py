from Body import Menu
import time
import os

os.system("clear")
Menu.loop()
url = 0
while url != 5:
    Menu.escolha()
    Menu.menu()
    try:
        url = input("OPÇÃO: ")
        if url == "1":
            url1 = input("URL: ")
            Menu.baixa()
            os.system(
                f"cd /data/data/com.termux/files/home/storage/shared/Movies && youtube-dl --audio-format mp3 {url1}")
            os.system("clear")
            continue
        elif url == "2":
            url1 = input("URL: ")
            Menu.baixa()
            os.system(
                f"cd /data/data/com.termux/files/home/storage/shared/Music && youtube-dl --extract-audio --audio-format mp3 {url1}")
            os.system("clear")
            continue
        elif url == "3":
            url1 = input("URL: ")
            Menu.baixa()
            os.system(
                f"cd /data/data/com.termux/files/home/storage/shared/Movies && youtube-dl -cit {url1}")
            os.system("clear")
            continue
        elif url == "4":
            os.system("clear")
            Menu.listaM()
            Menu.listaV()
            continue
        elif url == "5":
            url = url + 1
        else:
            os.system("clear")
            print("\033[1;31mOpcao Invalida... Tente Novamente\033[m")
    except:
        print("Bye")
        os.system("exit")
        break
