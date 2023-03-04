# 10/24 自己解出來的...JM 解答很好用！


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checker = set()
        res = ListNode(0, head)
        cur = res

        while cur.next:
            # 3/4 為何這裡可以不必寫 while cur and cur.next ??
            if cur.next.val in checker:
                cur.next = cur.next.next
            else:
                checker.add(cur.next.val)
                cur = cur.next
        return res.next


# Neetcode
class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            # 3/4 如果沒有while cur, cur = cur.next就會出問題...這又是為什麼呢？
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head