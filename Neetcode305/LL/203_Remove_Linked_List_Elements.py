# JM解法
class Solution(object):
    def removeElements(self, head, val):
    	cur = ListNode()
    	res = cur
    	cur.next = head
    # 直接modify head…亦可直接寫cur=ListNode(0,head)
    	while cur.next:
        	    if cur.next.val == val:
            	cur.next = cur.next.next
        	    else:
            	cur = cur.next
    	return res.next


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