# [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

```py
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        m = max(piles)
        
        while s <= m:
            k = (s + m) // 2
            t = sum(math.ceil(p / k) for p in piles)
            
            if t > h:
                s = k + 1
            else:
                m = k - 1

        return s
```