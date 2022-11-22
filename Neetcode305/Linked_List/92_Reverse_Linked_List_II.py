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
            # 10/30,11/3 !!!left-1!!!
            leftPrev, cur = cur, cur.next
        # 不是 lPrev.next=cur.next<--這樣node會跳掉第一個值！

        # Now cur="left",leftPrev="node before left"
        # 2)reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            # Change the pinter
            prev = cur
            cur = tmpNext

# 14:34
# 3) Updating the pointer(Connect leftPrev and prev)
# 10/23以下兩行不得置換 否則.next.next就會接錯...
        leftPrev.next.next = cur
        # e.g. Neetcode 11:00
        # [1,2,3,4,5]變「1,4,3,2,5」之後，curr pointer在5, prev在4,
        # 2 as the end of the reversed linked list,2.next目前為null,要怎麼銜接5?
        # 因為2沒有任何pointer，所以用leftPrev.next來指稱，然後再用.next來與5連結
        leftPrev.next = prev
        # 2（reversed前的舊head）和5連結後，1作為leftPrev可以用.next,來改跟4（reversed後的新head）連接了
        return dummy.next


#JS 解法：
# https://replit.com/@ZhangMYihua/M-N-reversals#index.js