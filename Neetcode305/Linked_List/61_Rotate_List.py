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
        # !! 3/27 length 從1開始！!
        while tail.next:
            # 10/24 和 2/14 不是tail
            tail = tail.next
            length += 1
        
        # 3/10 記得下面三行，處理ｋ
        k = k % length
        if k == 0:
            return head
        # 意思就是不用動
        
        #否則就是... Move to the pivot and rotate
        cur = head
        for i in range(length - k - 1):
            # 3/27 !!!不是length - k ＋ 1
            # 官方解答：
            # new head is in the position n - k, where n is a number of nodes in the list. The new tail is just before, in the position n - k - 1.
            cur = cur.next
        # 走完之後，用newHead儲值，作為新的起始點
        newHead = cur.next
        cur.next = None
        # 2/14切掉準備要放在前面的一段
        tail.next = head
        # 尾巴再跟頭接上...這樣豈非沒完沒了？JM:不會，上面做法直接改變原始的ＬＬ了

        return newHead
