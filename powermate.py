from winusbpy import *
from sendinput import PressKey, ReleaseKey, VK_LEFT, VK_RIGHT
from autoshiftcache import AutoShiftCache
import threading
import time
vid = "077d"
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
            dascache = 0    
            while True:
                data = api.read(0x81, 6)        
                offset = ord(data[1])
                print(offset)
                if offset > 127:
                    offset = -(256 - offset)
                    
                if offset != 0:
                    if dascache == 0:
                        dascache = offset
                    else:
                        if dascache > 0 and offset < 0:
                            dascache = 0
                        elif dascache < 0 and offset > 0:
                            dascache = 0
                        else:
                            dascache += offset
                while dascache >= 3:
                    dascache -= 3
                    PressKey(VK_RIGHT)
                    time.sleep(0.016)
                    ReleaseKey(VK_RIGHT)
                    print("RIGHT", dascache)
                while dascache <= -3:
                    dascache += 3
                    PressKey(VK_LEFT)
                    time.sleep(0.016)
                    ReleaseKey(VK_LEFT)
                    print("LEFT", dascache)
                    
if __name__ == "__main__":
    pmr = PowerMateReader()
    pmr.start()