class MaxList:
    def __init__(self):
        self.max_value = None
 
    def add(self, value):
        if self.max_value is None or value > self.max_value:
            self.max_value = value
 
    def max(self):
        return self.max_value
 
 
if __name__ == "__main__":
    m = MaxList()
    print(m.max()) # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max()) # 3
    m.add(8)
    m.add(5)
    print(m.max()) # 8