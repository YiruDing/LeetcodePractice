# 可以array或linked list解，後者較有效率
# 圖見7:21
# 每次加值都需要update pointer(s)


class ListNode:

    def __init__(self, val, nxt, prev):
        self.val = val
        self.next = nxt
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        cur = ListNode(value, self.right, self.right.prev)
        # !!!
        # 其前node為 self.right.prev
        self.right.prev.next = cur
        self.right.prev = cur
        # 重新定義self.right的前一個值（prev）
        # left --> right
        #      <--
        # e.g. 加入1
        # left --> 1 -->right
        #      <--   <--
        # e.g. 加入2
        # left --> 1 <--
        #            --> 2 <-- right
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        # e.g.刪除1
        # left --> 2 <-- right
        #      <--
        # 重新定義self.left.next.next與self.left的關係
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()