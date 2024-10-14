class Coloring:
    def __init__(self, n):
        self.graph = {i: [] for i in range(1, n + 1)}
        self.visited = {i: False for i in range(1, n + 1)}
        self.color = {i: None for i in range(1, n + 1)}
 
    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)
 
    def divisible_by_two(self, node, c):
        if self.visited[node]:
            return self.color[node] == c
        
        self.visited[node] = True
        self.color[node] = c
        
        for neighbor in self.graph[node]:
            if not self.divisible_by_two(neighbor, not c):
                return False
        return True
 
    def check(self):
        
        self.visited = {i: False for i in self.visited}
        self.color = {i: None for i in self.color}
        
        for node in range(1, len(self.graph) + 1):
            if not self.visited[node]:
                if not self.divisible_by_two(node, True):
                    return False
        return True
  
if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(3, 4)
    c.add_edge(1, 4)
    print(c.check()) # True
    c.add_edge(2, 4)
    print(c.check()) # False