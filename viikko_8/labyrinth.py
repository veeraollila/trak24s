def count(r):
    start = None 
    end = None
 
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == 'A':
                start = (i, j)  
            elif r[i][j] == 'B':
                end = (i, j) 
 
    if start is None or end is None:
        return -1
 
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
    def suitable(x, y):
        return 0 <= x < len(r) and 0 <= y < len(r[0]) and r[x][y] != '#'
 
    queue = [(start[0], start[1], 0)]
    visited = set() 
 
    while queue:
        x, y, dist = queue.pop(0)  
        if (x, y) == end:  
            return dist
 
        for dx, dy in moves:
            new_row, new_column = x + dx, y + dy
 
            if suitable(new_row, new_column) and (new_row, new_column) not in visited:
                queue.append((new_row, new_column, dist + 1))  
                visited.add((new_row, new_column))  
 
    return -1
 
if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7