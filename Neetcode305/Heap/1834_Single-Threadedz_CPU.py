# Use minHeap to sort the process time
class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])

        res = []
        minHeap = []
        i = 0
        # the current task we have added to our queue
        time = tasks[0][0]
        #tell us the current time. Starts with the smallest enqueue time
        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                # time >= tasks[i][0]代表任務已經進來了
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                                         # [process time, index]
                i += 1
            if not minHeap:
                # CPU is idling
                time = tasks[i][0]
                # fast forward to the enqueue time...可能一個是2,下個是9,那就直接快轉到9囉
            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        return res