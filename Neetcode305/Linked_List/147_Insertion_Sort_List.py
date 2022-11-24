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
