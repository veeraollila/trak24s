def count(grid):
    def dfs(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '#' or visited[x][y]:
            return
        visited[x][y] = True
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
 
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    room_count = 0
 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' and not visited[i][j]:
                dfs(i, j)
                room_count += 1
 
    return room_count
 
 
if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3