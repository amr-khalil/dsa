# Visualize the binary tree using graphviz
import graphviz


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def visualize(self, root):
        dot = graphviz.Digraph()
        self.add_nodes(root, dot)
        self.add_edges(root, dot)
        dot.render('./tree_graph', format='png', view=False)

    def add_nodes(self, node:Node, dot):
        if node is None:
            return
        dot.node(str(node.value))
        self.add_nodes(node.left, dot)
        self.add_nodes(node.right, dot)

    def add_edges(self, node:Node, dot):
        if node is None:
            return
        if node.left is not None:
            dot.edge(str(node.value), str(node.left.value))
        if node.right is not None:
            dot.edge(str(node.value), str(node.right.value))
        self.add_edges(node.left, dot)
        self.add_edges(node.right, dot)