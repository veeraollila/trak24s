def count(t):
    pricedoubled_count = {}
    ways_count = 0
 
    for i in range(len(t) - 1, -1, -1):
        ways_count += pricedoubled_count.get(t[i] * 2, 0)
        pricedoubled_count[t[i]] = pricedoubled_count.get(t[i], 0) + 1
    
    return ways_count
 
 
 
if __name__ == "__main__":
    print(count([1,2,3,4])) # 2
    print(count([1,1,1,1])) # 0
    print(count([1,2,1,2,1,2])) # 6
    print(count([5,1,3,4,1,6])) # 1