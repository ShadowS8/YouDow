from os import system

system("pkg install wget -y")
system("pkg install python -y")
system("pkg install ffmpeg -y")
system("curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /data/data/com.termux/files/usr/bin/youtube-dl")
system("chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl")
system("figlet PRONTO")
system("clear")
system("cd /data/data/com.termux/files/home/YouDow/Modulos && mv -v YouDow.py /data/data/com.termux/files/home/YouDow")
system("cd /data/data/com.termux/files/home/YouDow/ && mv -v YouDow /data/data/com.termux/files/home/YouDow/Modulos")
system("cd /data/data/com.termux/files/home/YouDow && python YouDow.py")
