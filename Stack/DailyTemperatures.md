# [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

```py
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and temp[i] >= temp[stack[-1]]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result
```