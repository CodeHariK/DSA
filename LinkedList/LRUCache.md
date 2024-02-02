# [146. LRU Cache](https://leetcode.com/problems/lru-cache/description/)

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

```py
class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity   
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)
        self.dict[key] = val   
        return val          
    def put(self, key: int, value: int) -> None:
        if key in self.dict:    
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]         
        self.dict[key] = value
```