# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

Given an integer array nums, find the subarray with the largest sum, and return its sum.

```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:     
        if not nums:
            return 0
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
```
