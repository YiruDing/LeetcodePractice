# HashMap userId-->HashSet to add/remove follower at O(1) time

# HashMap userId-->list of [count,TweetId]...
# "postTweet" could be just O(1) time
# but for "getNewFeed", I will have to keep track of time by using Heap
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.count = 0  # How many total tweets we have
        self.tweetMap = defaultdict(list)  #userId ->list of [count,tweetIds]
        self.followMap = defaultdict(set)  #userId -> set of followeeId
        # 亦可直接用hashＭap self.tweetMap={}
        # 但這樣之後就要再initialize it e.g.self.followMap[followeeId]=set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        # 3/10 因為用於minHeap,所以採用負數

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []  #Ordered starting from recent
        minHeap = []
        self.followMap[userId].add(userId)
        # Of course we all follow ourselves!

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # Get the most recent tweetId
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                # redefine them
                heapq.heappush(minHeap,
                               [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)