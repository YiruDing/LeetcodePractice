class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        result = ListNode(0, head)
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
