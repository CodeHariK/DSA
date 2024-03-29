# [2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/)

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

```py
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement,l = max(nums),0
        ans = 0
        count = 0

        for r,num in enumerate(nums):
            if num==maxElement:
                count+=1
            while count==k:
                if nums[l]==maxElement:
                    count-=1
                l+=1
            ans+=l

        return ans
```
