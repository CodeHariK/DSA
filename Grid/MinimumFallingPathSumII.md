# [1289. Minimum Falling Path Sum II](https://leetcode.com/problems/minimum-falling-path-sum-ii)

```py
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        for i in range(1,r):
            for j in range(c):
                grid[i][j] += min(grid[i-1][:j] + grid[i-1][j+1:])
                
        return min(grid[-1])
```
