from gpiozero import LightSensor

#Set variable of sensor to pin 18
sensor = LightSensor(18)

while True:
    sensor.wait_for_light()
    print("It's dark!")
    sensor.wait_for_dark()
    print("It's light!")
