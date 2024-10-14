class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
 
def count(node, depth=0):
    total_depth = depth
 
    for child in node.children:
        total_depth += count(child, depth + 1)
    return total_depth
 
if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])
 
    print(count(tree)) # 15