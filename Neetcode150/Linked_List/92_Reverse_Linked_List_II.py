# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head, left, right):
        i = 1
        arr = []
        h = head
        while head:
            if left == i:
                arr.append(head.val)
            elif left < i < right:
                arr.append(head.val)
            elif i == right:
                arr.append(head.val)
            print('Arr: ', arr)
            i += 1
            head = head.next
        j = 1
        head = h
        while head:
            if j == left:
                head.val = arr.pop(-1)
            elif left < j < right:
                head.val = arr.pop(-1)
            elif j == right:
                head.val = arr.pop(-1)
            head = head.next
            j += 1
        return h


ans = Solution()
ans.reverseBetween([1, 2, 3, 4, 5], 1, 4)
