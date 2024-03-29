* [46. Permutations](https://leetcode.com/problems/permutations/description/)

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path): 
            if not nums: 
                result.append(path) 
                return 
            for i in range(len(nums)): 
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) 
        result = [] 
        backtrack(nums, []) 
        return result 
```