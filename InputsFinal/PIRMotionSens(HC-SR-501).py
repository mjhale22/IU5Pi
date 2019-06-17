# Wiring diagram and tutorial can be found at: https://www.piddlerintheroot.com/pir-sensor/

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

led1 = 17
led2 = 27
pirPin = 26

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN)

def LIGHTS(pirPin):
    """Turns LEDS On and Off"""
    print("Motion Detected!")
    print("Lights on")
    GPIO.output(led1,GPIO.HIGH)
    GPIO.output(led2,GPIO.HIGH)

    time.sleep(2)

    print("Light off")
    GPIO.output(led1,GPIO.LOW)
    GPIO.output(led2,GPIO.LOW)

print("Motion Sensor Alarm (CTRL+C to exit)")
time.sleep(.2)
print("Ready")


try:
    GPIO.add_event_detect(pirPin, GPIO.RISING, callback=LIGHTS)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
