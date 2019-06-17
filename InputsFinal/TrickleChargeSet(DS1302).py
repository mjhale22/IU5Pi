#Wiring information can be found at: https://kevinsaye.wordpress.com/2017/12/22/adding-an-ds1302-to-a-raspberry-pi-zero-w/

#!/usr/bin/python
 
# Use the class for the DS1302 RTC chip.
import RTC_DS1302
import os
 
# Create an instance of the RTC class.
ThisRTC = RTC_DS1302.RTC_DS1302()
 
# Functions to write to the RTC chip.
dateString = os.popen('date +"%y %m %d %u %H %M %S"').read()
 
ThisRTC.WriteRAM('Last set: ' + os.popen('date +"%Y-%m-%d %H:%M:%S"').read().replace("\n", ""))
 
dateArray = dateString.split()
 
ThisRTC.WriteDateTime(int(dateArray[0]), int(dateArray[1]), int(dateArray[2]), int(dateArray[3]), int(dateArray[4]), int(dateArray[5]), int(dateArray[6]))
print 'Date set was: ' + dateString
 
DateTime = { "Year":0, "Month":0, "Day":0, "DayOfWeek":0, "Hour":0, "Minute":0, "Second":0 }
Data = ThisRTC.ReadDateTime(DateTime)
print 'Date read was: ' + Data
 
# Finish with the Raspberry Pi GPIO pins.
ThisRTC.CloseGPIO()
