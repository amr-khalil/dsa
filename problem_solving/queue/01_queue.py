

class Queue:
    def __init__(self) -> None:
        self.items = []
        
    def add(self, item):
        self.items.append(item)
    
    def remove(self):
        return self.items.pop(0)
    


if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    
    print(q.items)
    q.remove()
    print(q.items)