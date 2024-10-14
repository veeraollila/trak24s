class FastMode:
    def __init__(self):
        self.frequency = {}  
        self.mode_frequency = 0
        self.current_mode = None
 
    def add(self, x, k):
        self.frequency[x] = self.frequency.get(x, 0) + k
  
        if self.frequency[x] > self.mode_frequency or \
           (self.frequency[x] == self.mode_frequency and (self.current_mode is None or x < self.current_mode)):
            self.mode_frequency = self.frequency[x]
            self.current_mode = x
 
    def mode(self):
        return self.current_mode
 
 
if __name__ == "__main__":
    m = FastMode()
    m.add(4, 7)
    print(m.mode()) # 4
    m.add(8, 5)
    print(m.mode()) # 4
    m.add(8, 3)
    print(m.mode()) # 8
    m.add(4, 1)
    print(m.mode()) # 4