# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Optimal way. Go 2nd half of the array and reverse and compare with 1/2 half of the array.
        # There are definitely better solutions in discussion forum. I honestly think this is the easiest way to read the code.

        # T: O(N)
        # S: O(1)

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
