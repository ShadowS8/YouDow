import time
from os import system
def logo():
	while True:
	        system("clear")
	        print("Iniciando", end="")
	        print(".")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print("..")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print("...")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print(".")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print("..")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print("...")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print(".")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print("..")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print("...")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print(".")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print("..")
	        time.sleep (0.3)
	        system("clear")
	        print("Iniciando", end="")
	        print("...")
	        time.sleep (0.3)
	        system("clear")
	        break
system("clear")
logo()
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
		   [4] Enter (sair)
		<==================>
	""")
while True:
	menu()
	try:
		url = input("OPÇÃO: ")
		if url == "1":
			url1 = input("URL: ")
			print("Iniciando O Downloads...")
			system(f"youtube-dl --audio-format mp3 {url1}")
			system("clear")
			continue
		elif url == "2":
			url1 = input("URL: ")
			print("Iniciando O Downloads...")
			system(f"youtube-dl --extract-audio --audio-format mp3 {url1}")
			system("clear")
			continue
		elif url == "3":
			url1 = input("URL: ")
			print("Iniciando O Downloads...")
			system(f"youtube-dl -cit {url1}")
			system("clear")
			continue
	except:
		print("Bye")
		system("exit")
	break

