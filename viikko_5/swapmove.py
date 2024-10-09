def solve(t):
    commands = []
    n = len(t)
    
    order = t.copy()
    goal = list(range(1,n + 1))
 
    while order != goal:
        if order[0] > order[1] and order[1] != 1:
            commands.append('SWAP')
            order = [order[1]] + [order[0]] + order[2:]
 
        else:
            commands.append('MOVE')
            order = order[1:] + [order[0]]
 
    return commands
 
if __name__ == "__main__":
    print(solve([1, 2])) # esim. []
    print(solve([2, 1])) # esim. [SWAP]
    print(solve([1, 3, 2])) # esim. [SWAP, MOVE]
    print(solve([3, 2, 1])) # esim. [MOVE, SWAP]
    print(solve([2, 3, 4, 1])) # esim. [MOVE, MOVE, MOVE]