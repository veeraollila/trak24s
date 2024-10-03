def find(t):
    first_i = {}
 
    max_length = 0
 
    for i, num in enumerate(t):
        if num in first_i:
            distance = i - first_i[num] + 1  
            max_length = max( max_length, distance )
        else:
            first_i[num] = i
    
    if max_length == 0:
        return max_length
    else:
        return max_length - 1
 
 
if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4