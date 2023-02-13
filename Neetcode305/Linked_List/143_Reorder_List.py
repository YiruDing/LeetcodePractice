class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        #1  Because the slow list will stop running when fast reachs the end
        # So we can get the 1st half list then...
        slow, fast = head, head.next
        # 為何fast可為head 亦可為head.next?
        # 這只是先多跑一步而已，s位移後的index到時候還是一樣的
        # 10/17ＪＭ：除非你有dummy head當作起跑點,不然直接用head,起跑點必須不同
        # 可是兩個都可以pass...
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #2 reverse the second half of the list...
        # restart to run the rest of the list by moving the pointer
        second = slow.next
        prev = slow.next = None
        # 不能省略 reassigning the value of 'slow.next'，
        # 2/13ＪＭ：若非Ｎone,slow會一直指向3，之後就要處理1,2,3,4和3,4而非1,2和3,4的合併
        # 我之前的說法： 
        # 要截斷再重逢
        # Error - Found cycle in the ListNode
        # 如果是prev  = None，最後一個會指向Ｎone

        
        while second:
            tmp = second.next
            # Store the spot
            second.next = prev
            # Change the pointer
            prev = second
            second = tmp


# 印出來
# prev: ListNode{val: 4, next: ListNode{val: 3, next: None}}
# second: None
#3 Merge two halfs
        first, second = head, prev
        # a.k.a the 1st and 2nd list
        while second:
            tmp1, tmp2 = first.next, second.next
            # Modify these two links
            first.next = second
            second.next = tmp1
            # June 7 No more "first.next"! It's tmp1 that stored the value
            first, second = tmp1, tmp2
