class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        #  Because the slow list will stop running when fast reachs the end
        # So we can get the 1st half list then...
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the slow list...
        # restart to run the rest of the list by moving the pointer
        second = slow.next
        prev = slow.next = None
        # June 7 reassign the value of 'slow.next'
        while second:
            tmp = second.next
            # Store the spot
            second.next = prev
            # Change the pointer
            prev = second
            second = tmp


# Merge two halfs
        first, second = head, prev
        # a.k.a the 1st and 2nd list
        while second:
            tmp1, tmp2 = first.next, second.next
            # Modify these two links
            first.next = second
            second.next = tmp1
            # June 7 No more "first.next"! It's tmp1 that stored the value
            first, second = tmp1, tmp2
