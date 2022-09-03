# O(1)!
# L:LRU
# R:most recently use
# doble linked list & a hash map
# 7:23 全計畫


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev = node.prev,
        nxt = node.next
        # 抽掉node,prev直接接nxt
        prev.next = nxt
        nxt.prev = prev

# insert node at right

    def insert(self, node):
        # 示意圖見Ｎeetcode 16:19
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        # 插在中間後，再重新定義與prev和nxt的關係
        node.next = nxt
        node.prev = prev


# Get it in constant time

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            print(lru in self.cache)
            del self.cache[lru.key]