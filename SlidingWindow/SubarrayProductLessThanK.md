# [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

```py
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        l,product = 0,1

        for r,num in enumerate(nums):
            product *=num
            while product>=k and l<=r:
                product//=nums[l]
                l+=1
            ans+=r-l+1
        return ans
```
