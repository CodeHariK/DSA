# [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/description/)

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

```py
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len
```
