import socket
import os
TCP_IP = "10.42.0.1"
TCP_PORT = 5008
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
while 1:
	try:
		s.listen(1)
		conn, addr = s.accept()
		print("Connection adress: ", addr)
		data = (conn.recv(BUFFER_SIZE)).decode()
		duration = 1
		frequency = 500
		os.system("play --no-show-progress --null --channels 1 synth %s sine %f" % (duration,frequency))
		print(data)
	except KeyboardInterrupt:
		s.close()
