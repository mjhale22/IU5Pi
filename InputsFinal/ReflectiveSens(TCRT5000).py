#Wiring diagram and tutorial can be found at: https://www.modmypi.com/blog/how-to-use-the-tcrt5000-ir-line-follower-sensor-with-the-raspberry-pi

#!/usr/bin/python

from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

left_sensor = 11
right_sensor = 9

GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)

try:
	while True:
		if not GPIO.input(left_sensor):
			print("Robot is straying off to the right, move left captain!")
		elif not GPIO.input(right_sensor):
			print("Robot is straying off to the left, move right captain!")
		else:
			print("Following the line!")
		sleep(0.2)
except:
	GPIO.cleanup()
