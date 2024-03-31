# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            # if left is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target <nums[m]: 
                    r = m-1
                else:
                    l = m+1
            #right is sorted
            elif nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                
                else:
                    r = m-1
        
        return -1
```
