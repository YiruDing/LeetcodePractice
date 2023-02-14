# Solution in "heap"
# https://www.youtube.com/watch?v=q5a5OiGbT6Q
# 2/14lists本人是list 但 其內容為linked list!!
# 這個方法太耗時，第三個方法省時多了！！
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
            # 2/14 while!
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
# 10/24 JM:這樣若遇二值相同，還可以比較下一個值，而不會卡住
# 2/14 還沒看懂...
import heapq

class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h, counter = [], 0
        for ls in lists:
            if not ls:
                continue
            heapq.heappush(h, (ls.val, counter, ls))
            # heapq.heappush(heap, item)
            #(current.next.val, counter, current.next)
            counter += 1
            
        head = None
        while h:
            _, _, current = heapq.heappop(h)
            # (ls.val, counter, ls)
            head = head or current
            # current是linked list當下的頭，但是為何要加head?
            if current.next:
                heapq.heappush(h, (current.next.val, counter, current.next))
                counter += 1
            if h:
                current.next = h[0][2]
                # current.next的值
        return head
# Leetcode
# https://xn--leetcode-eo5g5b.com/problems/merge-k-sorted-lists/solutions/10919/python-easy-to-understand-divide-and-conquer-solution/?q=python&orderBy=most_votes
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next