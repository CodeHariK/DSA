# [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/description/)

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

```py
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b = 0,0
        for i in range(2,len(cost)):
            a, b = b, min(a + cost[i-2], b + cost[i-1])
        return min(a + cost[len(cost)-2], b + cost[len(cost)-1])
```
