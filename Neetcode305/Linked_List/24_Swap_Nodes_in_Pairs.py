# 圖見5:10


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # 記得(0,head)，不然過不了[1]這關
        prev = dummy
        curr = head

        while curr and curr.next:
            # Save pointers
            nxtPair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second
            # ！！prev.next不是curr而是second
            # 第一輪：這會是dummy head的開頭

            # Update pointers
            prev = curr
            curr = nxtPair
            # !!10/23 這順序不能亂，不然pre會等於nxtPair
        return dummy.next
