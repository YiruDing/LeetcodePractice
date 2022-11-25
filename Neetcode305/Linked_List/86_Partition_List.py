# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time O(1)space
# video 4:38
class Solution:

    def partition(self, head: Optional[ListNode],
                  x: int) -> Optional[ListNode]:
        res = ListNode()
        left = res
        later = ListNode()
        right = later
        # cur = head

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            #  !!!Update the node!!!
            else:
                right.next = head
                right = right.next
                #  !!!Update the node!!!
            head = head.next

        left.next = later.next
        # later is a dummy node
        right.next = None
        # Otherwise it will form a circle
        return res.next
