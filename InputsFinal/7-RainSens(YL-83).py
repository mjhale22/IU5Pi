#Wiring diagram and tutorial can be found at: https://raspi.tv/2017/make-a-rain-alert-system-with-raspberry-pi

# HIGH = no rain, LOW = rain detected
# Buzzer on GPIO13
from time import sleep
from gpiozero import Buzzer, InputDevice
 
buzz    = Buzzer(13)
no_rain = InputDevice(18)
 
def buzz_now(iterations):
    for x in range(iterations):
        buzz.on()
        sleep(0.1)
        buzz.off()
        sleep(0.1)
 
while True:
    if not no_rain.is_active:
        print("It's raining - get the washing in!")
        buzz_now(5)
        # insert your other code or functions here
        # e.g. tweet, SMS, email, take a photo etc.
    sleep(1)
