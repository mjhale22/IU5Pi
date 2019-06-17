#Wiring diagram and tutorial can be found at: https://www.electronicshub.org/interfacing-ir-sensor-with-raspberry-pi/
#Note that code below includes a buzzer to indicate when an object is in range but it is not necessary to use this sensor

import RPi.GPIO as GPIO
import time

sensor = 16
buzzer = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print "IR Sensor Ready....."
print " "

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,True)
          print "Object Detected"
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,False)


except KeyboardInterrupt:
    GPIO.cleanup()
