# Visualize the tree using graphviz
import graphviz


class Node :
    def __init__(self, value) -> None:
        self.value = value
        self.children: list[Node] = []
        
class Tree:
    def __init__(self, root) -> None:
        self.root = root
        
    def traverseBF(self):
        queue = [self.root]
        # so long as the queue is not empty
        # Take the first node from the queue
        while queue:
            current = queue.pop(0)
            print(current.value)
            queue.extend(current.children)
            print([q.value for q in queue])
            
    def traverseDF(self):
        stack = [self.root]
        
        while stack:
            current = stack.pop()
            print(current.value)
            # Extend the stack with children of the current node
            stack.extend(reversed(current.children))
            print([s.value for s in stack])
    
    def level_width(self):
        queue = [self.root, 's']
        counter = [0]
        while queue:
            current = queue.pop(0)
            if current == 's':
                queue.append('s')
                counter.append(0)
            else:
                queue.extend(current.children)
                counter[-1] += 1
        print(counter)
        
    def visualize(self):
        dot = graphviz.Digraph()
        self.add_nodes(self.root, dot)
        self.add_edges(self.root, dot)
        dot.render('./tree_graph', format='png', view=False)

    def add_nodes(self, node, dot):
        if node is None:
            return
        dot.node(str(node.value))
        # Iterate over children to add them as nodes
        for child in node.children:
            self.add_nodes(child, dot)

    def add_edges(self, node, dot):
        if node is None:
            return
        # Add edges from current node to its children
        for child in node.children:
            dot.edge(str(node.value), str(child.value))
            # Recursively add edges for children
            self.add_edges(child, dot)