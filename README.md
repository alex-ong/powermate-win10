# Griffin PowerMate for Windows 10

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
