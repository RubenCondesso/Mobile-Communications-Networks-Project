import logging
import time
import socket
logging.basicConfig(filename="/home/pi/Desktop/socket.log",level=logging.INFO)
logging.info("Socket program running")
TCP_IP = "192.168.0.1"
TCP_PORT = 5005
BUFFER_SIZE = 1024
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(11, GPIO.RISING)
logging.info("GPIO - Connecting to pin")

def action(pin):
        if GPIO.input(pin) == 1:
		MESSAGE = "Metal Detected"
		print("Raspberry 3 received sensor data")
		logging.info("Raspberry 3 received sensor data")
		return MESSAGE
	else:
		MESSAGE = "ND"
		return MESSAGE
logging.info("GPIO add_event_callback")
GPIO.add_event_callback(11, action)

while 1:
        try:
                #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#s.connect((TCP_IP, TCP_PORT))
		mess = action(11)
		if mess != "ND" :
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	                s.connect((TCP_IP, TCP_PORT))
			#s.connect((TCP_IP, TCP_PORT))
                	s.send(mess.encode())
			logging.info("Message sent to Raspberry 2")
        # except socket.error:
        #        logging.exception("Socket error!")
        #        pass
        except KeyboardInterrupt:
		logging.exception("Aborted! Closing connections")
                s.close()
                GPIO.cleanup()
                sys.exit()
                break

