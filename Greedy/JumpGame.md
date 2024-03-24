# [55. Jump Game](https://leetcode.com/problems/jump-game/description/)

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=target:
                target = i

        return target==0

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         gas = 0
#         for n in nums:
#             if gas < 0:
#                 return False
#             elif n > gas:
#                 gas = n
#             gas -= 1
            
#         return True
```
