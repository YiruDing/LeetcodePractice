# 1/27 不知道哪裡錯...
# trips: [[3, 2, 8], [4, 4, 6], [10, 8, 9]],capacity =11
class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda x: x[1])
        print('trips:', trips)
        # trips: [[3, 2, 8], [4, 4, 6], [10, 8, 9]]
        current_leave = []
        current_arrive = []
        guests = trips[0][0]
        heapq.heappush(current_arrive, [trips[0][1], trips[0][0]])
        heapq.heappush(current_leave, [trips[0][2], trips[0][0]])

        for i in range(1, len(trips)):
            leave = current_leave[0]
            arrive = current_arrive[0]

            if trips[i][1] >= leave[0]:
                guests -= leave[1]
                heapq.heappop(current_leave)
            if trips[i][2] <= arrive[0]:
                guests -= arrive[1]
                heapq.heappop(current_arrive)

            heapq.heappush(current_arrive, [trips[i][1], trips[i][0]])
            heapq.heappush(current_leave, [trips[i][2], trips[i][0]])
            guests += trips[i][0]
            print('!!!', guests)

            #!!! 7
            # !!! 13
        return guests <= capacity


# Leetcode看到的，很清爽的解法：
class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True
    
    dummy = ListNode(0, head)

        # 1) reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Now cur="left", leftPrev="node before left"
        # 2) reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # 3) Update pointers
        leftPrev.next.next = cur  # cur is node after "right"
        leftPrev.next = prev  # prev is "right"
        return dummy.next
    