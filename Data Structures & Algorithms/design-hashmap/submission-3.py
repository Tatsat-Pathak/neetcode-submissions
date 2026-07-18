class MyHashMap:
    bucket_size = 11

    def __init__(self):
        self.buckets = [[] for _ in range(self.bucket_size)]

    def put(self, key: int, value: int) -> None:
        bucket = key % self.bucket_size
        for index, (k, v) in enumerate(self.buckets[bucket]):
            if key == k:
                self.buckets[bucket][index] = (key, value)
                return
        
        self.buckets[bucket].append((key, value))
        return

    def get(self, key: int) -> int:
        bucket = key % self.bucket_size
        for k, v in self.buckets[bucket]:
            if key == k:
                return v
        
        return -1

    def remove(self, key: int) -> None:
        bucket = key % self.bucket_size
        for index, (k, v) in enumerate(self.buckets[bucket]):
            if key == k:
                self.buckets[bucket].pop(index)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)