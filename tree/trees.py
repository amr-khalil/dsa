from visualizer import Tree

        
        

class Node :
    def __init__(self, value) -> None:
        self.value = value
        self.children: list[Node] = []
    
    def add(self, value):
        self.children.append(Node(value))
        
    def remove(self, value):
        self.children = [child for child in self.children
                         if child.value != value]
        
        
root = Node(100)
root.add(50)
root.add(51)
root.add(52)
root.children[0].add(25)
# root.remove(51)

tree = Tree(root)
tree.level_width()
tree.visualize()