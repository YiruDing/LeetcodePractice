# Neetcode Doubly Linked List 為O(n)
class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    # O(1)
    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    # O(n)
    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    # O(n)
    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val


# Array Implementation
# stack/ DP array back & forward 為 O(1)
class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    # O(1)
    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            # make sure it's not out of bounce
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1
        # 3/9 不是 self.len += 1喔


# self.length 可能會比較大...
#     i -> 5
# 1 -> 2 -> 3 ->4
# 12:54 update the length(or pointer) 是為了forward fn...如果是array的話，我不太懂...

# O(1)

    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        # 3/9 不是 length - steps，因為是是從所在位置往前回溯
        return self.history[self.i]

    # O(1)
    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)
        # 3/9 不是 (length - steps,len(self.history) -1)
        return self.history[self.i]
