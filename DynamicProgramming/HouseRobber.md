# [198. House Robber](https://leetcode.com/problems/house-robber/description)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            a, b = b, max(b, a + num)
        
        return b
```
