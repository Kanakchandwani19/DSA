# Program for Least Recently Used (LRU) Page Replacement Algorithm

# Problem Statement:
# Implement the LRU (Least Recently Used) cache data structure.
# It should support the following operations:
# - get(key): Get the value of the key if it exists in the cache, otherwise return -1
# - put(key, value): Update or insert the value if the key is not present. When the cache
#   reaches its capacity, it should invalidate the least recently used item before inserting a new item.

# Both operations should run in O(1) time complexity.

# Examples:
# Example 1:
#   Input:
#   ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#   [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#   Output:
#   [null, null, null, 1, null, -1, null, -1, 3, 4]
#   Explanation:
#   LRUCache lRUCache = new LRUCache(2);
#   lRUCache.put(1, 1); // cache is {1=1}
#   lRUCache.put(2, 2); // cache is {1=1, 2=2}
#   lRUCache.get(1);    // return 1
#   lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
#   lRUCache.get(2);    // returns -1 (not found)
#   lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
#   lRUCache.get(1);    // return -1 (not found)
#   lRUCache.get(3);    // return 3
#   lRUCache.get(4);    // return 4

# Difficulty: Medium


class LRUCache:
    def __init__(self, capacity):
        # Write your code here
        # Hint: Use OrderedDict or implement using doubly linked list + hashmap
        pass

    def get(self, key):
        # Write your code here
        # Hint: If key exists, move it to front (most recently used)
        pass

    def put(self, key, value):
        # Write your code here
        # Hint: If at capacity and key doesn't exist, remove least recently used
        # Add/update key and move to front
        pass


# --- Run & Test ---
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))       # expected: 1
lru.put(3, 3)           # evicts key 2
print(lru.get(2))       # expected: -1
lru.put(4, 4)           # evicts key 1
print(lru.get(1))       # expected: -1
print(lru.get(3))       # expected: 3
print(lru.get(4))       # expected: 4
