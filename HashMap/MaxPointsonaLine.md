# [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/description/)

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

```py
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        ans = 1
        for a in range(l):
            pa = points[a]
            count = defaultdict(int)
            for b in range(a+1,l):
                pb = points[b]

                if pa[0] == pb[0]:
                    slope = float('inf')
                else:
                    slope = (pa[1] - pb[1])/(pa[0] - pb[0])
                count[slope] += 1
                ans = max(ans, count[slope] + 1) 
        return ans
```
