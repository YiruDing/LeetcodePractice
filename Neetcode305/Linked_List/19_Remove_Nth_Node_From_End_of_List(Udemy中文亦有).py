class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        result = ListNode(0, head)
        # Thst's where left starts...It's not nessesary to be 0
        # And the neaxt is head
        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        left = result
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

# Move the right pointer to the "right" place
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return result.next


# 3/27 我寫的，待改（下有正確版）
# if not head:return head
#         length = 1
#         cur = head
#         while cur:
#             cur = cur.next
#             length += 1

#         if length == 1 and n >=1:
#             return None

#         n = n % length

#         if n == 0:
#             return head

#         cur = head
#         for i in range(length - n - 2):
#             cur = cur.next
#         if cur and cur.next:
#             cur.next = cur.next.next

#         return head


# 正確版
class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        sz = 0
        node = head

        while node:
            node = node.next
            sz += 1

        # it's guaranteed that 1 <= n <= sz
        if n == sz:
            return head.next
        else:  # 2 <= n <= sz -1

            node = head
            prev, curr = node, node.next
            for _ in range(sz - n - 1):
                prev, curr = curr, curr.next
            prev.next = prev.next.next
            return head
