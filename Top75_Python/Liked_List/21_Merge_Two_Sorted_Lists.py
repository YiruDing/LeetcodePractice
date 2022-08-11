# https://www.youtube.com/watch?v=XIdigk956u0


def mergeTwoLists(self, list1, list2):
    result = ListNode()
    tail = result
    #8/8JM: 一個是假頭（dummy head），可以讓while loop不用處理例外...a.k.a.包進特殊的case，否則就要先跑一次if list1.val < list2.val
    # 得先比大小才能得到真的頭，比較麻煩。

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return result.next
