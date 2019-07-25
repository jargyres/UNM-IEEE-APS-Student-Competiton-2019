# UNM-IEEE-APS-Student-Competiton-2019 ![UNM Antennas Logo](https://raw.github.com/jargyres/UNM-IEEE-APS-Student-Competiton-2019/master/Gui/src/Antennaslogo.png) 



This project was the University of New Mexico's submission for the IEEE AP/S 2019 Student Design Competition. The prompt was to *"Propose a setup that characterizes/demonstrates the properties of an antenna system and provide educational material to explain these properties."*

This project went to place third at IEEE AP/S 2019, you can read about it [here](https://engineering.unm.edu/news/2019/07/ece-team-wins-third-place-in-design-contest.html).


For our project we decided to use Lego Mindstorms parts to create a turntable capable of doing 3D Radiation Patterns for an antenna. We used a 2 antenna setup were the antenna under test (AUT) was put on the Lego turntable and we took a known antenna and placed it in another Lego device to hold it. We then, using a software defined radio (SDR), transmit a signal from the AUT and look at the received power at the known antenna. We can then mark down the power and degree the AUT was at and create a 2D radiation pattern for the antenna.

The next part of our testing was to take the S11 of the antenna, which is the reflected power of the antenna across a span of frequencies. We accomplished this by using a dual directional coupler.

Check out our video below showing the full project and results.
[![UNM-IEEE-sPS-2019](https://raw.github.com/jargyres/UNM-IEEE-APS-Student-Competiton-2019/master/Images/youtube-Thumbnail.png)](https://www.youtube.com/watch?v=l86pVJDWy_k)

**[Required Materials](#required-materials)**<br>
**[Installation Instructions](#installation-intructions)**<br>
**[Usage Instructions](#usage-instructions)**<br>
**[Compatibility](#compatibility)**<br>
**[Authors and Acknowledgments](#authors-and-acknowledgments)**<br>



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

### Python Code

To get the code working on python, clone the repoitory into the Raspberry Pi, then move the Raspberry Pi Scripts into the home directory of the Raspberry Pi. It must either be in the home folder, or you will need to edit the shell scripts to call the absolute path of the python scripts.

## Usage Instructions

### S11 Measurement

We need to do the S11 measurement first to see the resonant frequency of the AUT.

   * To do this you need to change directory to the "Executables" folder. Then run the command
     ```
     sudo chmod a+x GeneralizedS11Measurement
     ```
     This will make our S11 Measurment file executable so that we can run it from the command line.
     
   * Once the file is executable, plug in the BladeRF SDR into your computer.
   
        We need to change the serial string on GeneralizedS11Bash.sh
        
        To do this enter bladeRF-cli by entering
        
        ```
        bladeRF-cli -e info
        ```
        
        You should then see a string for the "Serial #"
        
        Copy that string and change line 156 in GeneralizedS11Bash.sh to the new serial
        
   * We can also have to plug in our AUT into the "output" port of the coupler, plug the transmitting end into the "input" and the receiving end at the correct ports according the video.
        
        
   * To run GeneralizedS11Bash.sh type
     ```
     sudo /path/to/script/GeneralizedS11Bash
     ```
     
     This will run the S11 script
     
   * Now we run the script, we are prompted to set our desired variables
     * Frequency
     
          This will be the center frequency of the test. Enter frequency in Hz.
          
     * Resolution
          
          The resolution is the distance between samples. High is a sample every 1 MHz step, Medium is 5 Mhz steps, Low is 10 MHz steps.
     
     * Bandwidth
          
          The bandwidth is the size of the span of frequencies we will sweep across. For example, if you set your center frequency to 3 GHz and the badnwidth to 600 MHz, the sweep would be from 2.7 GHz to 3.3 GHz.
   
   * When part one is finished, swap the load and the receiving port and enter "yes" to the prompt. This will automatically start part 2 of the test. When this is done a matplotlib graph will show up of your S11 Measurement. This will also leave a file "finalS11.csv", which is in the form <frequency (in Hz), return loss> 
               
   
   
### Radiation Pattern Measurement

To begin the radiation pattern measurement, we need to set up the raspberry pi and our laptop. 

   * Raspberry pi
     
     When we call our python scripts to control the lego turntable, we are using the secure shell (SSH) protocol. This is called during the bash scripts. Due to this we need to have an IP address from the raspberry pi. There are a couple ways of doing this. The way we did it was setting up isc-dhcp-server on our Ubuntu laptop. This let us directly connect to the raspberry pi through a ethernet cable by setting a static IPv4 address to our ethernet adapter. This lets us always keep the scripts the same as the IP address never changes. You could also just manually find the IP address and edit the scripts.
     
   * Turntable
   
      the turntable needs to have its motors plugged into the BrickPi 3 to control them. To do this plug the motor that controls the Bottom into the "MA" port, the motor that controls the top portion into "MB" and the color sensor into "S1"
      
   * Now we are ready to run the script. To run enter
        ```
        sudo /path/to/script/GeneralizedRadiationPattern <frequency>
        ```
        
        Enter the frequency in the same way as the S11 script, in Hz. 
        
        The script will start running and display a live polar plot of the radiation pattern. When it is done the script will leave a csv file in the form of <degree, power (db)>

### Compatibility

Our scripts will be able to run in any bash shell, such as the ones that come with macOS Mojave and most Linux distributions. 


### Authors and Acknowledgments

* **John Argyres**
* **Arjun Gupta**
* **Ralph Lyndon Gesner**

Special thanks to IEEE for the funding of this project. To the University of New Mexico for their facilities and people who helped us along the way. 

