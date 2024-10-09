def solve(t):
 
    moves = 0
    middle = len(t) // 2
    if len(t) % 2 != 0:  
        middle += 1 
 
    if sorted(t) == t:
        return 0
 
    for i, j in enumerate(t):
        if i < middle and j > middle:
            moves += (middle - i)
        elif i >= middle and j <= middle:
            moves += (i - middle)
    return moves
 
if __name__ == "__main__":
    print(solve([2, 1, 4, 3])) # 0
    print(solve([5, 3, 4, 1, 6, 2])) # 6
    print(solve([6, 5, 4, 3, 2, 1])) # 9
    print(solve([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])) # 15
