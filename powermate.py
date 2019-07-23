from winusbpy import *
from sendinput import PressKey, ReleaseKey, VK_LEFT, VK_RIGHT
from autoshiftcache import AutoShiftCache
import threading
import time

vid = "077d" #vid and pid of powermate usb.
pid = "0410"


class PowerMateReader(threading.Thread):
    def __init__(self):
        self.shiftCache = AutoShiftCache()
        threading.Thread.__init__(self)
        
    def run(self):   
        api = WinUsbPy()    
        result = api.list_usb_devices(deviceinterface=True, present=True)
        
        if result:            
            if api.init_winusb_device(vid, pid):
                while True:                
                    data = api.read(0x81, 6) #read 6 bytes. 
                    buttonDown = ord(data[0])
                    offset = ord(data[1])
                    self.shiftCache.updatePush(buttonDown == 1)
                        
                    if offset > 127:
                        offset = -(256 - offset)
                    
                    if offset > 0:
                        self.shiftCache.increment(offset)
                    elif offset < 0:
                        self.shiftCache.decrement(-offset)
                
            else:
                print ("device not found. Here are the available devices:")
                for p in api.device_paths:                   
                    print (p[8:25])
                    
if __name__ == "__main__":
    pmr = PowerMateReader()
    pmr.start()
    while True:
        if not pmr.isAlive():
            break
        pmr.shiftCache.tick(time.time())
    print ("Device not found, or disconnected. Exiting")