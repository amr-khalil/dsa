"""
implement funtionality of hashmap (get and put), then he asked me to make it thread safe.
"""

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * self.size
        
    def get_hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self.get_hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = HashNode(key, value)
        else:
            node = self.buckets[index]
            while node.next:
                node = node.next
            node.next = HashNode(key, value)
    
    def get(self, key):
        index = self.get_hash(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

import threading

class ThreadSafeHashMap(HashMap):
    def __init__(self, size=10):
        super().__init__(size)
        self.locks = [threading.Lock() for _ in range(self.size)]
        
    def get(self, key):
        index = self.get_hash(key)
        with self.locks[index]:
            return super().get(key)
        
    def put(self, key, value):
        index = self.get_hash(key)
        with self.locks[index]:
            super().put(key, value)

    

if __name__ == '__main__':
    h = ThreadSafeHashMap()
    h.put('a', 1)
    h.put('b', 2)
    h.put('c', 3)
    print(h.get('a'))
    print(h.get('b'))
    print(h.get('c'))
    print(h.get('d'))
    
    