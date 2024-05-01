# [355. Design Twitter](https://leetcode.com/problems/design-twitter/)

```py
class Twitter:
    def __init__(self):
        self.followMap = collections.defaultdict(set)
        self.postMap = collections.defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.count, tweetId])
        self.count-=1 #Just for creating the max-heap 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            for post in self.postMap[user]:
                heap.append(post)
        heapq.heapify(heap)
        while heap and len(res)<10:
            count, tweet = heapq.heappop(heap)
            res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
```
