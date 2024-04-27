# [514. Freedom Trail](https://leetcode.com/problems/freedom-trail)

```py
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        dp = defaultdict(int)

        def backtrack(i,j):
            if i==len(key):
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            res = float('inf')
            for k,c in enumerate(ring):
                if c==key[i]:
                    minDist = min(abs(k-j),n-abs(k-j))
                    res = min(res,1+minDist+backtrack(i+1,k))
                    
            dp[(i,j)]=res
            return res

        return backtrack(0,0)
```
