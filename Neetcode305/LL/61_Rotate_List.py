# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def rotateRight(self, head: Optional[ListNode],
                    k: int) -> Optional[ListNode]:
        if not head:
            return head

        # Get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Move to the pivot and rotate
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        # 抓到新起始點
        cur.next = None
        # 切掉準備要放在前面的一段
        tail.next = head
        # 尾巴再跟頭接上...這樣豈非沒完沒了？JM:不會，上面做法直接改變原始的ＬＬ了

        return newHead

