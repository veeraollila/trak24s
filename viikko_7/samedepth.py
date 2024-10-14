class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
 
def check(node, depth=0, leaf_depths=None):
    if leaf_depths is None:
        leaf_depths = set()
        
    if not node.children:
        leaf_depths.add(depth) 
        return len(leaf_depths) == 1
    
    else:
        return all(check(child, depth + 1, leaf_depths) for child in node.children)
 
if __name__ == "__main__":
    tree1 = Node(1, [
                Node(2),
                Node(3, [Node(4, [Node(5), Node(6)])]),
                Node(7, [Node(8), Node(9)])
            ])
 
    tree2 = Node(1, [Node(2, [Node(3)]), Node(4, [Node(5), Node(6)])])
 
    print(check(tree1)) # False
    print(check(tree2)) # True