def create(n, k):
    list = [i + 1 for i in range(n)]
    counter, i, j = 0, 0, 0
    
    while i < k:
        if j == n - 1 - counter:
            j = 0
            counter += 1
            continue
        hold = list[j]
        list[j] = list[j + 1]
        list[j + 1] = hold
 
        j, i = j + 1, i + 1
 
    return list
 
if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # [1,3,2]
    print(create(3, 2)) # [3,1,2]
    print(create(10, 34))