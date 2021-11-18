# Agilent N5766A Interface

## Connecting to the Power Supply
1) The power supply must be connected via LAN
2) The LAN LED on the front of the power supply should be on
3) Get the power supply's IP address by pressing the LAN button on the front of the power supply.
     * It should be of the form 169.254.*
     * Usually it is 169.254.95.52
4) Enter the IP address into a browser and it should take you to the powersupply's website.
    * You can change all the settings from the "Browser Web Control" tab found in the upper left-hand corner of the page.

## Getting the Software Setup
If you haven't done so, clone this repository on the computer that will be communicating with the power supply.
You will need to use Google Chrome for this to work!
1) Download [chromedriver](https://sites.google.com/chromium.org/driver/downloads) into this repository
2) Install the selenium python library
    * `pip install selenium`

## Using the Interface
