# [2958. Length of Longest Subarray With at Most K Frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/)

You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

```py
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        count = defaultdict(int)

        for r,num in enumerate(nums):
            count[num]+=1
            while count[num]>k:
                count[nums[l]]-=1
                l+=1
            ans = max(ans,r-l+1)

        return ans
```
