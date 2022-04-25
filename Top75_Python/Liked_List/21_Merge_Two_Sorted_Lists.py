# https://www.youtube.com/watch?v=XIdigk956u0


def mergeTwoLists(self, list1, list2):
    result = ListNode()
    tail = result

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
