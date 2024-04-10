# [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

```py
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-1 * x for x in stones]

        heapify(stones)

        while(len(stones) > 1):
            b = heappop(stones)
            s = heappop(stones)

            if(b - s != 0):
                heappush(stones, -abs(b-s))

        return abs(heappop(stones)) if len(stones) == 1 else 0
```
