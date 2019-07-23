# UNM-IEEE-APS-Student-Competiton-2019 ![UNM Antennas Logo](https://raw.github.com/jargyres/UNM-IEEE-APS-Student-Competiton-2019/master/Gui/src/Antennaslogo.png) 

This project was the University of New Mexico's submission for the IEEE AP/S 2019 Student Design Competition. The prompt was to *"Propose a setup that characterizes/demonstrates the properties of an antenna system and provide educational material to explain these properties."*


For our project we decided to use Lego Mindstorms parts to create a turntable capable of doing 3D Radiation Patterns for an antenna. We used a 2 antenna setup were the antenna under test (AUT) was put on the Lego turntable and we took a known antenna and placed it in another Lego device to hold it. We then, using a software defined radio (SDR), transmit a signal from the AUT and look at the received power at the known antenna. We can then mark down the power and degree the AUT was at and create a 2D radiation pattern for the antenna.



**[Required Materials](#required-materials)**<br>
**[Installation Instructions](#installation-intructions)**<br>
**[Usage Instructions](#usage-instructions)**<br>
**[Troubleshooting](#troubleshooting)**<br>
**[Compatibility](#compatibility)**<br>


## Required Materials

### Software Defined Radio
* You will need the following materials to get started with the measurements.
     The code is designed to work with a Nuand BladeRF Software Defined Radio (SDR) whic you can get [here](https://www.nuand.com/product/bladerf-x115/).
* We used the bladeRFx115 for our experiments, if you decide to use another model, you may need to modify the bash scripts to support your model.

### BrickPi 3
* To control the Lego Mindstorms motors, we used a BrickPi3 from Dexter Industries, this connects to our Raspberry Pi 3 and gives us multiple inputs for plugging the motors into. 

* You can grab the base kit [here](https://www.dexterindustries.com/product/brickpi-advanced-for-raspberry-pi/) ,which only contains the BrickPi unit and power supply.

     Alternatively you can get the Starter Pack [here](https://www.dexterindustries.com/product/brickpi-starter-kit/) , which contains the BrickPi unit, Raspberry Pi 3, and the preloaded micro SD card.



## Installation Intructions

### bladeRF-cli

To control the BladeRF SDR, we need to download bladeRF-cli, the command line interface for the BladeRF.


We can


## Dependencies

### BladeRF

### Python

* To get started, you will need to use pip to download the necessary packages.

     To see insructions on how to download pip click [here](https://pip.pypa.io/en/stable/installing/)
     
* Download numpy and matplotlib to your python. 

     ```
     sudo pip install numpy
     ```
     
     ```
     sudo pip install matplotlib
     ```
### Setting up the BrickPi

To use the BrickPi libraries, we need to use Raspbian for Robots, a Debian based Linux distro for the Raspberry Pi and BrickPi.

To do, navigate to [Dexter Industries](https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/) main site for details onto burning Raspbian for Robots onto the SD card. 

## Usage Instructions

## Compatibility

### Troubleshooting
