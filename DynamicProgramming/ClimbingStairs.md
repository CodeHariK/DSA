# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```py
class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        a,b = 1,2
        for i in range(2,n-1):
            a,b = b, a + b
        return a + b
```
