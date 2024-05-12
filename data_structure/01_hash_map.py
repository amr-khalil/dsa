"""
Hash Map
- Key-value pair
- Keys are unique
- Keys are immutable
- Keys are hashable

Hash Function types:
- Arthmetic modular method, example: hash(key) = key % table_size
- Truncation method, example: hash(key) = key % 1000
- Folding method, example: hash(key) = sum of digits of key

Collision Handling:
- Separate chaining, example: linked list
- Linear probing, example: hash(key) = (hash(key) + 1) % table_size
- Quadratic probing, example: hash(key) = (hash(key) + i^2) % table_size
- Resizing the List, example: double the size of the list

Time Complexity:
- Insert: O(1)
- Search: O(1)
- Delete: O(1)
Space Complexity: O(n)
"""


class HashMap:
    def __init__(self) -> None:
        self.size = 10
        self.bucket = [None] * self.size
        
    def get_hash(self, key):
        return hash(key) & 5
    
    def put(self, key, value):
        hash_key = self.get_hash(key)
        if self.bucket[hash_key] is None:
            self.bucket[hash_key] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.bucket[hash_key]):
                if k == key:
                    del self.bucket[hash_key][i]
                    break
            self.bucket[hash_key].append((key, value))
        
    def get(self, key):
        hash_key = self.get_hash(key)
        for i, (k,v) in enumerate(self.bucket[hash_key]):
            if k == key:
                return self.bucket[hash_key][i][1]
   
    def remove(self, key):
        hash_key = self.get_hash(key)
        for i, (k, v) in enumerate(self.bucket[hash_key]):
            if k == key:
                del self.bucket[hash_key][i]
                


class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class HashMap2:
    def __init__(self):
        self.size = 10
        self.bucket = [None] * self.size
        
    def get_hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        hash_key = self.get_hash(key)
        if self.bucket[hash_key] is None:
            self.bucket[hash_key] = HashNode(key, value)
        else:
            node = self.bucket[hash_key]
            while node.next:
                node = node.next
            node.next = HashNode(key, value)
        
    def get(self, key):
        hash_key = self.get_hash(key)
        node = self.bucket[hash_key]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None
    
    def remove(self, key):
        hash_key = self.get_hash(key)
        node = self.bucket[hash_key]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.bucket[hash_key] = node.next
                return
            prev = node
            node = node.next
        return None
    
if __name__ == '__main__':
    hmap = HashMap2()
    hmap.put("1", "a")
    hmap.put(2, "x")
    hmap.put(11, "b")
    hmap.put(11, "c")
    print(hmap.get(11))
    print(hmap.bucket)
    print(hmap.remove(1))
    print(hmap.bucket)