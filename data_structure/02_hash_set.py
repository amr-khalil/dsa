class HashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def get_hash(self, key):
        return key % self.size
    
    def put(self, key):
        hash_key = self.get_hash(key)
        if key not in self.buckets[hash_key]:
            self.buckets[hash_key].append(key)
                
    def get(self, key):
        hash_key = self.get_hash(key)
        if self.buckets[hash_key] is not None:
            for k in self.buckets[hash_key]:
                if k == key:
                    return True
        return False
    
    def remove(self, key):
        hash_key = self.get_hash(key)
        if self.buckets[hash_key] is not None:
            for i, k in enumerate(self.buckets[hash_key]):
                if k == key:
                    del self.buckets[hash_key][i]
                    break
        
    
if __name__ == '__main__':
    hash_set = HashSet()
    hash_set.put(1)
    hash_set.put(2)
    print(hash_set)
    print(hash_set.contains(1))
    hash_set.remove(1)
    print(hash_set)
    print(hash_set.contains(1))
    print(hash_set.contains(2))
    print(hash_set.contains(3))