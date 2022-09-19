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


# Neetcode
# Break the pointer,re-connect to prev
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int,
                       right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # 1)Reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Now cur="left",leftPrev="node before left"
        # 2)reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev = cur
            cur = tmpNext

# 14:34
# 3) Updating the pointer(Connect leftPrev and prev)
        leftPrev.next.next = cur
        leftPrev.next = prev
        return dummy.next


#JS 解法：
# https://replit.com/@ZhangMYihua/M-N-reversals#index.js