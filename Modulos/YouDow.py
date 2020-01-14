from Modulos.Body import Menu
import time
from os import system
system("clear")
Menu.loop()
while True:
	Menu.menu()
	try:
		url = input("OPÇÃO: ")
		if url == "1":
			url1 = input("URL: ")
			Menu.baixa()
			system(f"youtube-dl --audio-format mp3 {url1}")
			system("clear")
			continue
		elif url == "2":
			url1 = input("URL: ")
			Menu.baixa()
			system(f"youtube-dl --extract-audio --audio-format mp3 {url1}")
			system("clear")
			continue
		elif url == "3":
			url1 = input("URL: ")
			Menu.baixa()
			system(f"youtube-dl -cit {url1}")
			system("clear")
			continue
	except:
		print("Bye")
		system("exit")
	break

