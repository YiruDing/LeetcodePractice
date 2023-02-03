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
