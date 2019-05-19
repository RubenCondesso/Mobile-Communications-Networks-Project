import socket
import sys
import logging
logging.basicConfig(filename="/home/pi/socket.log",level=logging.INFO)
logging.info("Socket program running")
TCP_IP = "192.168.0.1"
TCP_PORT = 5005
BUFFER_SIZE = 1024

TCP_IP_PC = "10.42.0.1"
TCP_PORT_PC = 5008
BUFFER_SIZE_PC = 1024
i=0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logging.info("Client socket created")
s.bind((TCP_IP, TCP_PORT))
logging.info("Binding done, IP: {}, Port: {}".format(TCP_IP, TCP_PORT))

while 1:
	try:
		s.listen(1)
		logging.info("Listening...")
		print("Listening...")
		conn, addr = s.accept()
		logging.info("Connection address: {}".format(addr))
		data = (conn.recv(BUFFER_SIZE)).decode()
		if not data:
			print("empty message")
			logging.warning("Empty message received!")
		else:
			logging.info("Message received: {}".format(data))
			logging.info("Message number: {}".format(i))
			print("Message number: ",i)
			i = i + 1
			s_PC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s_PC.connect((TCP_IP_PC, TCP_PORT_PC))
			s_PC.send(data.encode())
			logging.info("Message sent to PC")
			s_PC.close()

	except socket.error:
		logging.exception("Socket error!")
		pass
	except KeyboardInterrupt:
		logging.exception("Aborted! Trying to close connections")
		try:

			s.close()
			s_PC.close()
		except:
			pass
		logging.exception("Connections closed. Terminating program")
		sys.exit(1)
	except:
		logging.exception("Error: {}".format(sys.exc_info()[0]))
		try:
			s.close()
			s_PC.close()
		except:
			pass
		raise
