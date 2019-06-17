Recommended: Method 2: .bashrc 
This method to run a program on your Raspberry Pi at startup is to modify the .bashrc file. With the .bashrc method, your python program will run on boot and also every time when a new terminal is opened.


In terminal type the following command: 
sudo nano /home/pi/.bashrc


Go to the last line of the script (below "fi") and add the following lines: 
xhost + 
echo Running at boot 
sudo python /home/pi/sample.py


#The "sudo python" line above must be editied to the location and name of the file that you wish to run at startup
