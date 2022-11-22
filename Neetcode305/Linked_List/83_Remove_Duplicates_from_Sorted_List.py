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
            if cur.next.val in checker:
                cur.next = cur.next.next
            else:
                checker.add(cur.next.val)
                cur = cur.next
        return res.next