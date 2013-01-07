import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ports = [11, 12, 15]

def setup(port):
	GPIO.setup(port, GPIO.OUT)

def on(port):
	GPIO.output(port, True)

def off(port):
	GPIO.output(port, False)

def init(ports):
	for i in ports:
		setup(i)

def blink(port):
	on(port)
	time.sleep(1)
	off(port)
	time.sleep(1)

def lightshow(ports):
	while True:
		for i in ports:
			on(i)
			time.sleep(1)
		for i in ports:
			off(i)
			time.sleep(1)

init(ports)
lightshow(ports)
