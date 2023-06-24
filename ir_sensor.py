import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.IN)
val = 0

while True:
	inter = GPIO.input(3) ^ 1
	if val == 500:
		print("true")
		break
	else:
		val += inter
	time.sleep(0.01)
