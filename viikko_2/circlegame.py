def create(n):
    circle = list(range(1, n + 1))
    order = []
    i = 0
    
    while circle:
        i = (i + 1) % len(circle)
        order.append(circle.pop(i))
    
    return order
 
 
if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,3,5,7]
    print(create(6)) # [2, 4, 6, 3, 1, 5]
    print(create(2)) # [2, 1]
    print(create(4)) # [2, 4, 3, 1]