# [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/description)

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

```py
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def subarraysWithAtMost(kEle):
            freq = defaultdict(int)
            l = ans = 0

            for r,num in enumerate(nums):
                freq[num]+=1
                while len(freq)>kEle:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1
                
                ans+=r-l+1
            
            return ans

        return subarraysWithAtMost(k)-subarraysWithAtMost(k-1)
```
