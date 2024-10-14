class Mex:
    def __init__(self):
        self.elements = set()
        self.current_mex = 0
 
    def add(self, x):
        self.elements.add(x)
        
        while self.current_mex in self.elements:
            self.current_mex += 1
            
        return self.current_mex
 
 
if __name__ == "__main__":
    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6