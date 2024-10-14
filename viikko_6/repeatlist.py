class RepeatList:
    def __init__(self):
        self.values = set() 
        self.repeat = False 
 
    def add(self, x):
        if x in self.values:
            self.repeat = True
        else:
            self.values.add(x)
 
    def check(self):
        return self.repeat
    
if __name__ == "__main__":
    r = RepeatList()
    print(r.check()) # False
    r.add(1)
    r.add(2)
    r.add(3)
    print(r.check()) # False
    r.add(2)
    print(r.check()) # True
    r.add(5)
    print(r.check()) # True