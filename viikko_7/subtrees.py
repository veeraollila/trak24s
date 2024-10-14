class Node:
    def __init__(self, value, children = None):
        self.value = value
        self.children = children if children is not None else []
 
def count(node):
    def count_nodes(node):
        if not node.children:
            return 1
        return 1 + sum(count_nodes(child) for child in node.children)
 
    def check_subtrees(node):
        if not node.children:
            return True
        
        return len(set(count_nodes(child) for child in node.children)) == 1
 
    def count_nodes(node):
        count = 0
        if check_subtrees(node):
            count += 1
        for child in node.children:
            count += count_nodes(child)
        
        return count
 
    return count_nodes(node)
 
 
if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])
 
    print(count(tree)) # 8
 
    tree = Node(4, [Node(1), Node(3, [Node(2)])])
    print(count(tree)) # 3
 
    tree = Node(3, [Node(2, [Node(1)])])
    print(count(tree)) # 3