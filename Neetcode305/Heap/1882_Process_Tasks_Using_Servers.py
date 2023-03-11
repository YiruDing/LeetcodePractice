class Solution:

    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)

        available = [(servers[i], i) for i in range(len(servers))]
        # Available Servers [wieght,index]
        heapq.heapify(available)
        unavailable = []

        t = 0
        for i in range(len(tasks)):
            t = max(t, i)

            if len(available) == 0:
                t = unavailable[0][0]
                # 如果大家都很忙，就加上最小的available time，然後繼續往前走
            while unavailable and t >= unavailable[0][0]:
                # t >= unavailable[0][0] 代表可以開始處理任務
                freetims, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)
            res[i] = index
            heapq.heappush(unavailable, (t + tasks[i], weight, index))
            # Unavailable Servers [available time, weight, index]
        return res