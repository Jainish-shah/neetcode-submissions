class node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = node(0,0), node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
           self.remove(self.cache[key])
           self.insert(self.cache[key])
           return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # check for the existance of the key otherwise add
        # check capacity 
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = node(key, value)
        self.insert(self.cache[key])

        if self.capacity < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


