#Wiring diagram and tutorial can be found at: https://www.piddlerintheroot.com/dht11/

#PRIOR TO RUNNING, TYPE FOLLOWNING INTO TERMINAL:
#   git clone https://github.com/adafruit/Adafruit_Python_DHT.git
#   sudo pip3 install Adafruit_DHT
#   cd Adafruit_Python_DHT
#   sudo apt-get update

#Import Adafruit_DHT Sensor Library to use code associated with sensor
import Adafruit_DHT

# Set variable of sensor to (sensor being used) DHT11 : Options are DHT11, DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set variable of gpio as pin 14
gpio=14

#Identify variables being pulled from Adafruit_DHT library (import Adafruit_DHT)
humidity, temperature = Adafruit_DHT.read(sensor, gpio)

#Set temperatureF to convert temperature (celsius) to fahrenheit
#Previous script (line 17) identifying "temperature" from library must be listed above this line of code
temperatureF=(temperature*(9/5)+32)
 
if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperatureF, humidity))
else:
  print('Failed to get reading. Try again!')

