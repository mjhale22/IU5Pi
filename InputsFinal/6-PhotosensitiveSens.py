from gpiozero import LightSensor

#Set variable of sensor to pin 18
sensor = LightSensor(18)

#Code below works properly but does not make sense?
while True:
    sensor.wait_for_light()
    print("It's dark!")
    sensor.wait_for_dark()
    print("It's light!")
