# ThreeSum

[15. ThreeSum](https://leetcode.com/problems/3sum/description/)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = defaultdict()

        def twosum(arr: List[int], target):
            s = 0
            l = len(arr) - 1

            while (s < l):
                ss = arr[s]
                ll = arr[l]
                if(ss + ll > target):
                    l -= 1
                elif (ss + ll < target):
                    s += 1
                else:
                    ans[str([-target, ss, ll])] = [-target, ss, ll]
                    s += 1

        for i in range(len(nums)-2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                twosum(nums[i+1:] ,-nums[i])

        return map(lambda x: ans[x], ans)
```
