class NearList:
    def __init__(self, t):
        self.sorted = sorted(t)
 
    def find(self, x):
        if x <= self.sorted[0]:
            return self.sorted[0]
        
        if x >= self.sorted[-1]:
            return self.sorted[-1]
 
        limit_low, limit_high = 0, len(self.sorted) - 1
 
        while limit_low <= limit_high:
            middle = (limit_low + limit_high) // 2
  
            if self.sorted[middle] == x:
                return x
 
            elif x < self.sorted[middle]:
                limit_high = middle - 1
 
            else:
                limit_low = middle + 1
        
        if self.sorted[limit_low] - x < x - self.sorted[limit_high]:
            return self.sorted[limit_low]
        else:
            return self.sorted[limit_high]
 
        
if __name__ == "__main__":
    n = NearList([3, 6, 1, 3, 9, 8])
    print(n.find(1)) # 1
    print(n.find(2)) # 1
    print(n.find(3)) # 3
    print(n.find(4)) # 3
    print(n.find(5)) # 6
    print(n.find(6)) # 6
    print(n.find(7)) # 6
    print(n.find(8)) # 8
    print(n.find(9)) # 9