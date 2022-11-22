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
        # 抽掉node(定位),prev直接接nxt（賦值）
        prev.next = nxt
        nxt.prev = prev

# insert node at right

    def insert(self, node):
        # 示意圖見Ｎeetcode 16:19
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        # 插在中間後(定位)，再重新定義與prev和nxt的關係（賦值）
        node.next = nxt
        node.prev = prev


# Get it in constant time

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        # 為何可以用cache[key]直接找到對應的node?linkedlist可以這樣操作嗎？
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
            # 可以請你談談 del嗎？我目前找到的資料提到，
            # “python有GC机制，所以，del语句作用在变量上，而不是数据对象上。”
            # 這是什麼意思啊？
            # https://blog.csdn.net/love1code/article/details/47276683
            
# 另解，還是有用到del
#出處：https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList
class Node:
def __init__(self, k, v):
    self.key = k
    self.val = v
    self.prev = None
    self.next = None

class LRUCache:
def __init__(self, capacity):
    self.capacity = capacity
    self.dic = dict()
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head

def get(self, key):
    if key in self.dic:
        n = self.dic[key]
        self._remove(n)
        self._add(n)
        return n.val
    return -1

def set(self, key, value):
    if key in self.dic:
        self._remove(self.dic[key])
    n = Node(key, value)
    self._add(n)
    self.dic[key] = n
    if len(self.dic) > self.capacity:
        n = self.head.next
        self._remove(n)
        del self.dic[n.key]

def _remove(self, node):
    p = node.prev
    n = node.next
    p.next = n
    n.prev = p

def _add(self, node):
    p = self.tail.prev
    p.next = node
    self.tail.prev = node
    node.prev = p
    node.next = self.tail