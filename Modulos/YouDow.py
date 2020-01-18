from Modulos.Body import Menu
import time
import os
os.system("clear")
Menu.loop()
url = 0
while url != 5:
    Menu.menu()
    try:
        url = input("OPÇÃO: ")
        if url == "1":
            url1 = input("URL: ")
            Menu.baixa()
            os.system(f"youtube-dl --audio-format mp3 {url1}")
            os.system("clear")
            continue
        elif url == "2":
            url1 = input("URL: ")
            Menu.baixa()
            os.system(f"youtube-dl --extract-audio --audio-format mp3 {url1}")
            os.system("clear")
            continue
        elif url == "3":
            url1 = input("URL: ")
            Menu.baixa()
            os.system(f"youtube-dl -cit {url1}")
            os.system("clear")
            continue
        elif url == "4":
            os.system("clear")
            Menu.lista()
            continue
        elif url == "5":
            url = url + 1
        else:
            os.system("clear")
            print("Opcao Invalida... Tente Novamente")
    except:
        print("Bye")
        os.system("exit")
        break

