

class AutoShiftCache(object):    
    def __init__(self):
        self.counter = 0
        self.delay = 0.016
        self.sensitivity = 1 #higher numbers = less sensitive
        
    #Increment. can be by a negative amount
    def increment(self, amount):
        pass
        
    def tick(self, timestamp):
        pass
        

        