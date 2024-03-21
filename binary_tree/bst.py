from visualizer import BinaryTree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value and self.left:
            self.left.insert(value)
        elif value < self.value:
            self.left = Node(value)
        elif value > self.value and self.right:
            self.right.insert(value)
        else:
            self.right = Node(value)
    
    def contains(self, value):
        if value == self.value:
            return True
        if value < self.value and self.left:
            return self.left.contains(value)
        elif value > self.value and self.right:
            return self.right.contains(value)
        return False
            
            
btree = Node(10)
btree.insert(5)
btree.insert(20)
btree.insert(800)
btree.insert(200)
btree.insert(18)

tree = BinaryTree()
tree.visualize(btree)





