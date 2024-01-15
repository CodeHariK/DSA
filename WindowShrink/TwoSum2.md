# TwoSum2

[167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

## Go

```Go
    func twoSum(numbers []int, target int) []int {
        s := 0
        l := len(numbers) - 1

        for s < l {
            sum := numbers[s] + numbers[l]

            if sum > target {
                l--
            } else if sum < target {
                s++
            } else {
                return []int{s + 1, l + 1}
            }
        }
        return []int{}
    }
```

## Java

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int s = 0;
        int l = numbers.length - 1;

        while (s < l) {
            int sum = numbers[s] + numbers[l];

            if (sum > target) {
                l--;
            } else if (sum < target) {
                s++;
            } else {
                return new int[]{s + 1, l + 1};
            }
        }
        return new int[0];
    }
}
```

## C++

```c++
class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& numbers, int target) {
        int s = 0;
        int l = numbers.size() - 1;

        while (s < l) {
            int sum = numbers[s] + numbers[l];

            if (sum == target) {
                return {s + 1, l + 1};
            } else if (sum < target) {
                s++;
            } else {
                l--;
            }
        }
        return {};
    }
};
```

## Py

```py
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = dict()

        s = 0
        l = len(numbers) - 1

        while s < l:
            sum = numbers[s] + numbers[l]
                
            if sum > target:
                l -= 1
            elif sum < target:
                s += 1
            else :
                return [s + 1, l + 1]
```
