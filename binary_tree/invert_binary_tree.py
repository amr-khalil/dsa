from visualizer import visualize_binary_tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(51)
root.left.right = Node(52)
root.left.right.right = Node(53)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

visualize_binary_tree(root)