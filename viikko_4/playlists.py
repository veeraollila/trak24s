def count(t):
    last = {}
    start = 0
    total = 0
 
    for i, track in enumerate(t):
        if track in last and last[track] >= start:
            start = last[track] + 1
 
        last[track] = i
        total += i - start + 1
 
    return total
 
 
if __name__ == "__main__":
    print(count([1,2,3,4])) # 10
    print(count([1,1,1,1])) # 4
    print(count([5])) # 1
    print(count([1,3,2,3,4,2,4,1,2,1])) # 24