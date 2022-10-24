class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = ListNode()
        x = curr
        while head:
            if head.val == val and head.next is None:
                # !!10/23 是 is None
                curr.next = head.next
                curr = curr.next
                head = head.next
                break
            # 處理最後一個值為val的狀況
            if head.val == val:
                # print(1)
                head = head.next
            else:
                # print(2)
                curr.next = head
                # 不是curr.next=head.next
                curr = curr.next
                head = head.next
                continue
        return x.next