#Wiring diagram and tutorial can be found at: https://tutorials-raspberrypi.com/configure-and-read-out-the-raspberry-pi-gas-sensor-mq-x/

#PRIOR TO RUNNING, TYPE FOLLOWNING INTO TERMINAL:
#   git clone https://github.com/tutRPi/Raspberry-Pi-Gas-Sensor-MQ
#   Python files can now be found in File Manager > Raspberry-Pi-Gas-Sensor-MQ

from mq import *
import sys, time

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
        sys.stdout.flush()
        time.sleep(0.1)

except:
    print("\nAbort by user")
