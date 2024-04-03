

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, data):
        self.head = Node(data, self.head)
        
    def insert_last(self, data):
        if not self.head:
            self.head = Node(data)
            return
        
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)
        
    def size(self):
        """
        Node => Node => Node => None, then size = 3
        """
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
        
    def get_first(self):
        return self.head.data
    
    def get_last(self):
        if not self.head:
            return None
        
        node = self.head
        while node:
            if not node.next:
                return node.data
            node = node.next
            
    def clear(self):
        self.head = None
        
    def remove_first(self):
        if not self.head:
            return
        
        self.head = self.head.next
        
    def remove_last(self):
        if not self.head:
            return
        
        if not self.head.next:
            self.head = None
            return
        
        node = self.head
        while node:
            if not node.next.next:
                node.next = None
                return
            node = node.next
            
        def remove_n
    
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.insert_first(2)
    ll.insert_first(3)
    ll.insert_first(6)
    ll.remove_first()
    ll.print_list()