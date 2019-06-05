# Assembly Instructions

### Software

#### Connecting to the pi

* Apply power to the raspberry pi through the USB power port
* Wait for the pi to boot, indicated by the 'ready' LED
* Connect to the pi's wifi network on the chosen device
* Connect to the VeinCam server through a web browser on the chosen device
* Press the 'on' switch to activate the camera  

#### Changing the user parameters 

* To change the base URL: 
    - Change the `10.0.0.5` variable in the autohotspot launch script

* To change the wifi name:
    - ssh into the pi 
    - Run: `cd /etc/`
    - Run: `nano hostname`
    - Change the host name
    - When finished press `ctrl + x`, `Y`, `Enter`
