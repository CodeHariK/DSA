# 1. [Two Sum](https://leetcode.com/problems/two-sum/description/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Go

```Go
func twoSum(nums []int, target int) []int {
    var m = make(map[int]int)
    for i := 0; i < len(nums); i++ {
        if index, ok := m[target - nums[i]]; ok {
            return []int{index, i}
        }
        m[nums[i]] = i
    }
    return []int{}
}
```

## Java

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = target - nums[i];
            if (map.containsKey(num)) {
                return new int[]{map.get(num), i};
            }

            map.put(nums[i], i);
        }

        return new int[0];
    }
}
```

## C++

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (numMap.count(complement)) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }

        return {}; // No solution found
    }
};
```

## Py

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}
      for i, num in enumerate(nums):
        complement = target - num
        if num in seen:
          return [i, seen[num]]
        seen[complement] = i

      return []
```
