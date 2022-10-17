# Solution in "heap"
# https://www.youtube.com/watch?v=q5a5OiGbT6Q


class Solution:

    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            # We will keep on reducing it
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
            # mergedLists as a variable
        return lists[0]

    def mergeList(self, L1, L2):
        result = ListNode()
        tail = result

        while L1 and L2:
            if L1.val < L2.val:
                tail.next = L1
                L1 = L1.next
            else:
                tail.next = L2
                L2 = L2.next
            tail = tail.next
            # 這裡的tail.next就是從上面取得的值
            #！！tail 也要往下走，才不會只在原地更改值

        if L1:
            tail.next = L1
        if L2:
            # Not elif!!
            tail.next = L2
        return result.next

    # Not tail.next!!


# 下解...
# 搭配heap來找出最小值，這個我懂，但是用counter是為什麼呢？
import heapq


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h, counter = [], 0
        for ls in lists:
            if not ls:
                continue
            heapq.heappush(h, (ls.val, counter, ls))
            # heapq.heappush(heap, item)
            # Push the value item onto the heap, maintaining the heap invariant.
            # 為何item長這個樣子(current.next.val, counter, current.next)？？
            print("h:", h)
            # 一次append一組Linked list??
            # h: [(1, 0, ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}})]
            # h: [(1, 0, ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}), (1, 1, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}})]
            # h: [(1, 0, ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}), (1, 1, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}), (2, 2, ListNode{val: 2, next: ListNode{val: 6, next: None}})]

            counter += 1
        head = None
        while h:
            _, _, current = heapq.heappop(h)
            # (ls.val, counter, ls)
            head = head or current
            # current是linked list唷
            if current.next:
                heapq.heappush(h, (current.next.val, counter, current.next))
                counter += 1
            if h:
                current.next = h[0][2]
                # current.next的值
        return head