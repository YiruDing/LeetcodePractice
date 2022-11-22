class Solution:

    def insertionSortList(self,
                          head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = head, head.next

        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                # 不需換順序，只要換pointer
                continue

            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next
                # 繼續往前走，找到插入點
            prev.next = cur.next
            cur.next = tmp.next
            # assign tmp.next before reassign it
            tmp.next = cur
            cur = prev.next
            #  prev.next 就是 cur.next

        return dummy.next
