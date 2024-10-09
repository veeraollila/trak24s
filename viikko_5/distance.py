def find(t, k):
    t = sorted(t)
    biggest_dist = 0
    
    for i in range(1, len(t)):
        dist = (t[i] - t[i - 1]) // 2  
        biggest_dist = max(biggest_dist, dist)  
    
    biggest_dist = max(biggest_dist, t[0] - 1, k - t[-1])
    return biggest_dist
 
 
if __name__ == "__main__":
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970