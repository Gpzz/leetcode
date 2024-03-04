#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

# Create a Node class for doubly linked list
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

# Least Recently Used cache - left, right = LRU, MRU
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Hashmap to store key value and corresponding node object
        self.cache = {}
        # Initialise with empty left & right nodes to track LRU & MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # Remove node from list by updating pointers of neighbourhood nodes
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


    def insert(self, node):
        # Insert at MRU using self.right.prev node to track current MRU
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        # Remove & Insert updates position to MRU
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Remove LRU using self.left.next node to track current LRU
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

