# [3068. Find the Maximum Sum of Node Values](https://leetcode.com/problems/find-the-maximum-sum-of-node-values)

```py
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = [(num^k)-num for num in nums]
        delta.sort(reverse=True)
        ans = sum(nums)

        for i in range(0,len(nums)-1,2):
            path = delta[i]+delta[i+1]
            if path<=0:
                break
            ans+=path

        return ans
```
