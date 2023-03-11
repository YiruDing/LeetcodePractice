# MaxHeap, Queue
#minimize idle time
class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # Basiclly is a hashmap to store all the numbers of letters
        # https://www.wongwonggoods.com/python/python-counter/
        maxHeap = [-cnt for cnt in count.values()]
        # 只需要值，不需管key了
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        # To trace the info needed
        # pairs of [-cnt剩幾個字母/task要處理，idleTime間隔]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                # 3/10 一次處理掉一個task,可以用1+ 負數 來表示
                if cnt:
                    q.append([cnt, time + n])
                    # 8:28 time+n:
                    # Check what time is this task going to be available for us to process once again
            if q and q[0][1] == time:
                # !!time值一直滾動調整
                # 3/10 " q and"不可省略，否則會出現以下警訊：deque index out of range
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

    # maxHeap:-3,-2,-2,
    #         -2,-1,-1,
    #         -1,
    # q:[-2,2],[-1,3],[-1,4]
    #   [-1,5]

    # 8/7
    # while time=1 cnt=1+(-3) q.append[-2,2]
    # while time=2 cnt=1+(-2）q.append[-1,3]，此時因為q[0][1] == time，maxHeap要push[-2]
    # while time=3 cnt=1+(-2）q.append[-1,4]，maxHeap要push[-1]
    # while time=4 cnt=1+(-2）q.append[-1,5]，maxHeap要push[-1]
    # while time=5 cnt=1+(-1）cnt為0，不必計算idle期，所以不用加入q：maxHeap要push[-1]
    # while time=6 cnt=1+(-1）cnt為0，不必加入q,剩0個task，不用加進maxHeap裡面
    # while time=7 cnt=1+(-1) maxHeap已空，跳過第一次if statement，q has nothing to popleft,either
    # RETURN 7
    # YAAAAY!
