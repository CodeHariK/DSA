# 1. [Two Sum](https://leetcode.com/problems/two-sum/description/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}
      for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:
          return [i,seen[comp]]
        seen[num] = i
```
