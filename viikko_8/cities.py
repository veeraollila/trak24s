class Cities:
    def __init__(self, n):
        self.roads = {i: set() for i in range(1, n + 1)}
 
    def add_road(self, a, b):
        self.roads[a].add(b)
        self.roads[b].add(a)
 
    def has_route(self, a, b):
        visited = set()
        queue = [a]
 
        while queue:
            current = queue.pop(0)
            if current == b:
                return True
            
            if current not in visited:
                visited.add(current)
                queue.extend(self.roads[current] - visited)
        
        return False
 
if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1, 2)
    c.add_road(1, 3)
    c.add_road(4, 5)
    print(c.has_route(1, 5)) # False
    c.add_road(3, 4)
    print(c.has_route(1, 5)) # True