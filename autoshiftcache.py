from sendinput import *
def clamp(smol, big, value):
    value = max(smol,min(value,big))
    return value
#override this class to make your input work.
class InputHandler(object):    
    def __init__(self):
        self.counter = 0
        self.isPushed = False        
        
    #Increment. can be by a negative amount
    def increment(self, amount):
        pass
        
    def decrement(self, amount):
        pass
    
    def updatePush(self, pushValue):
        self.isPushed = pushValue
        
    def tick(self, timestamp):
        pass

#Auto shifting handler. changing direction instantly stops.
SIXTY_HZ = 1.0/60
SENSITIVITY = 8
SHIFT_MAX = 6
class AutoShiftCache(InputHandler):
    def __init__(self):
        super(AutoShiftCache, self).__init__()
        #pushlength is one cycle.
        #scroll-length is 0.016
        self.lastMessageTime = 0
        self.currentTime = 0
        self.leftIsDown = False
        self.rightIsDown = False
        self.lastWheelTime = 0
        self.rawCounter = 0
    def increment(self, amount):
        if self.counter < 0:
            self.counter = 0
        else:
            self.rawCounter += amount
            while self.rawCounter > SENSITIVITY:
                self.rawCounter -= SENSITIVITY
                self.counter += 1
        self.counter = clamp(0,SHIFT_MAX,self.counter)
        
        self.lastMessageTime = self.currentTime
    
    def decrement(self, amount):
        if self.counter > 0:
            self.counter = 0
        else:
            self.rawCounter -= amount
            while self.rawCounter < -SENSITIVITY:
                self.rawCounter += SENSITIVITY
                self.counter -= 1
                
        self.counter = clamp(-SHIFT_MAX,0,self.counter)
        self.lastMessageTime = self.currentTime
        
    def tick(self, timestamp):
        delta = timestamp - self.currentTime
        eventDelta = timestamp - self.lastWheelTime
        if self.counter > 0:
            if self.leftIsDown:
                ReleaseKey(VK_LEFT)
            if eventDelta >= SIXTY_HZ:            
                if self.rightIsDown:
                    print("releaseRight")
                    ReleaseKey(VK_RIGHT)    
                    self.rightIsDown = False
                    self.counter -= 1
                else: #right isnt down.
                    PressKey(VK_RIGHT)                    
                    print("PressRight")
                    self.rightIsDown = True
        
                self.lastWheelTime = timestamp
        elif self.counter < 0:
            if self.rightIsDown:
                ReleaseKey(VK_RIGHT)
            if eventDelta >= SIXTY_HZ:            
                if self.leftIsDown:
                    print("releaseLeft")
                    ReleaseKey(VK_LEFT)    
                    self.leftIsDown = False
                    self.counter += 1
                else: #right isnt down.
                    PressKey(VK_LEFT)                   
                    print("PressLeft")
                    self.leftIsDown = True
        
                self.lastWheelTime = timestamp
                
        else: # self.counter == 0:
            if self.rightIsDown:
                ReleaseKey(VK_RIGHT)
                self.lastWheelTime = timestamp
            if self.leftIsDown:
                ReleaseKey(VK_LEFT)
                self.lastWheelTime = timestamp
                
        self.currentTime = timestamp