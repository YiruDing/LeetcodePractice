class Solution:

    def insertionSortList(self,
                          head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # !!ListNode(0, head)
        prev, cur = head, head.next

        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                # 不需換順序，只要換pointer
                continue
            # 3/10 走到需要變動的地方
            tmp = dummy
            # 逆向回去確認前值
            while cur.val > tmp.next.val:
                # !!不是tmp.val
                tmp = tmp.next
                # 勿忘這兩行！
                # 繼續往前走，找到插入點
            prev.next = cur.next
            # prev跟下下一個接在一起了
            cur.next = tmp.next
            # assign tmp.next before reassign it
            # cur指向上一個，也就是交換位置swap
            tmp.next = cur
            # tmp指向cur，完成swap
            cur = prev.next
            #  prev.next 就是 cur.next

        return dummy.next


class Solution:

    def insertionSortList(self,
                          head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sentinel = ListNode()
        curr = head
        while curr:
            prev = sentinel
            while prev.next and curr.val >= prev.next.val:
                prev = prev.next

            curr.next, prev.next, curr = prev.next, curr, curr.next

        return sentinel.next