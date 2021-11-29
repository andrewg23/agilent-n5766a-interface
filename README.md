# Agilent N5766A Interface

## Quick Refference
`python psCommand.py -p X -v X -c X`
* `-p` or `--power`   ->  Set Power status, 1 on, 0 off
* `-v` or `--voltage` -> Set Voltage
* `-c` or `--current` -> Set current

## Connecting to the Power Supply
1) The power supply must be connected via LAN
2) The LAN LED on the front of the power supply should be on
3) Get the power supply's IP address by pressing the LAN button on the front of the power supply
     * It should be of the form 169.254.*
     * Usually it is 169.254.95.52
4) Enter the IP address into a browser and it should take you to the powersupply's website.
    * It may take few minutes for the website to be available
    * You can change all the settings from the "Browser Web Control" tab found in the upper left-hand corner of the page

## Getting the Software Setup
If you haven't done so, clone this repository on the computer that will be communicating with the power supply.  
You will need to use Google Chrome for this to work!
1) Download [chromedriver](https://sites.google.com/chromium.org/driver/downloads) into `/agilent-n5766a-interface`
    * The path to the driver should be `/agilent-n5766a-interface/chromedriver`
3) Install the selenium python library
    * `pip install selenium`

## Using the Interface
* Simply run `python psCommand.py` to get the status of the power supply
* Add on any of the optional flags to change the state:
    1) Set Power status
        * `-p` or `--power`
    2) Set Voltage
        * `-v` or `--voltage`
    4) Set current
       * `-c` or `--current`
