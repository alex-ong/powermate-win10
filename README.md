# Griffin PowerMate for Windows 10

**Note: Please try the project at the [bottom](#other-projects) first! It doesnt require re-installing the Driver with WinUSB**

This repository is a simple way to reprogram the Griffin powermate, that works in windows 10.
We first override the Griffin powermate driver with WinUSB, which is a generic user-space driver. 

Then, we use python to interface with the raw powermate's signals, and output whatever keyboard/mouse events we want.
This is all done in user-space (rather than kernel space), meaning it is easy to re-define what we want to send.

# Installation / Usage

1. Install python 2.7 (https://www.python.org/downloads/release/python-2716/)
2. Plug in Griffin power mate (only usb supported)
3. run Zadig (`tools/`)
 * `Options` -> `Show All Devices`
 * Select `Griffin power mate`
 * Select `WinUSB (v6.1.7600.16385)`
 * `Install driver`
4. Install WinUsbPy (`tools/`)
 * Unzip `WinUsbPy-master.zip`
 * open a cmd console to the unzipped directory 
 * use `python setup.py install` (alternative is `py -2 setup.py install` if running multiple python installs) 
5. Run it
 * `python powermate.py` or if you have multiple installs, `py -2 powermate.py`
 
To edit the functionality, have a look at autoshiftcache.py, and implement the `increment`, `decrement` and `tick` functions.
I have included a stripped down `sendinput.py`, which allows you to send windows keyboard events.


# Uninstalling / Reverting (oh no, it doesnt work :( )
* Open Device manager
* Select Griffin power mate
* Update driver
* Choose from drivers
* Try each of the different drivers (the one that worked for me wasn't called Griffin Powermate, it was called "USB Input Device")
* ![image](https://user-images.githubusercontent.com/6406312/124419461-e1ef6300-dda0-11eb-935f-0237e921f3ce.png)
* Open Griffin powermate official software again, it should work with one of the drivers



### Other projects 
These projects are also in python2, and have been confirmed to work on other people's systems:
It uses the **default** powermate driver; therefore not needing WinUSB override.
 * https://github.com/crash7/griffin-powermate
   * Python 2.7.9+

| Commands to run                              | python2 installed             | python2 and python3 installed          |
|----------------------------------------------|-------------------------------|----------------------------------------|
| Install pywinusb                             | pip install pywinusb          | py -2 -m pip install pywinusb          |
| Install griffin_powermate                    | pip install griffin_powermate | py -2 -m pip install griffin_powermate |
| Run test file (you need to write one first!) | python test.py                | py -2 test.py                          |
   






