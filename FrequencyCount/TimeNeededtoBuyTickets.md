# [2073. Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets)

```py
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(k+1):
            ans+=min(tickets[i],tickets[k])

        for i in range(k+1,len(tickets)):
            ans+=min(tickets[i],tickets[k]-1)

        return ans
```
