# [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/description/)

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

```py
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         ans = [9999] * len(nums)
#         ans[0] = 0

#         for i in range(len(nums) - 1):
#             for j in range(nums[i]):
#                 if i + j + 1 < len(nums):
#                     ans[i+j+1] = min(ans[i] + 1, ans[i+j+1])

#         return ans[-1]

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        curr_end,curr_far = 0,0
        for i in range(len(nums)-1):
            curr_far = max(curr_far,i+nums[i])
            if i==curr_end:
                ans+=1
                curr_end = curr_far

        return ans
```
