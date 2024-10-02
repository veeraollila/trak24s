def count(t):
    min_value = min(t)
    
    first = t.index(min_value)
    
    last = len(t) - 1 - t[::-1].index(min_value)
    
    possibilites = last - first
    
    return possibilites
 
if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0