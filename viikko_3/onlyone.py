def find(t):
    numbers = {}
 
    for number in t:
        numbers[number] = numbers.get(number, 0) + 1
 
    for number, count in numbers.items():
        if count == 1:
            return number
 
 
if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5