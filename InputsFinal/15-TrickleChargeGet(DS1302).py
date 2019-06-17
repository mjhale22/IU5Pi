#Wiring information can be found at: https://kevinsaye.wordpress.com/2017/12/22/adding-an-ds1302-to-a-raspberry-pi-zero-w/

#!/usr/bin/python
 
# Use the class for the DS1302 RTC chip.
import RTC_DS1302
import os
 
# Create an instance of the RTC class.
ThisRTC = RTC_DS1302.RTC_DS1302()
 
# Functions to read from the RTC chip.
# print("RAM: " + ThisRTC.ReadRAM())
 
DateTime = { "Year":0, "Month":0, "Day":0, "Hour":0, "Minute":0, "Second":0 }
Data = ThisRTC.ReadDateTime(DateTime)
 
DateSetResponse = os.popen("date -s \"" + Data + "\"").read()
 
print "Time has been set to: " + DateSetResponse
 
# Finish with the Raspberry Pi GPIO pins.
ThisRTC.CloseGPIO()
