class MyHashSet:
    bucket_size = 5

    def __init__(self):
        self.buckets = [[] for _ in range(self.bucket_size)]

    def add(self, key: int) -> None:
        bucket = key % self.bucket_size
        if key not in self.buckets[bucket]:
            self.buckets[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = key % self.bucket_size
        if key in self.buckets[bucket]:
            self.buckets[bucket].remove(key)

    def contains(self, key: int) -> bool:
        bucket = key % self.bucket_size       
        return key in self.buckets[bucket]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)