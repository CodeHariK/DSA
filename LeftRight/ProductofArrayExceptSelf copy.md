# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Go

```Go
func productExceptSelf(nums []int) []int {
    result := make([]int, len(nums))
    
    product := 1
    for i := len(nums) - 1; i >= 0; i-- {
        result[i] = product
        product *= nums[i]
    } 
    
    product = 1
    for i := 0; i < len(nums); i++ {
        result[i] *= product
        product *= nums[i]
    }
    return result
}
```

## Java

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int result[] = new int[n];
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }
        int suffixProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffixProduct;
            suffixProduct *= nums[i];
        }

        return result;
    }
}
```

## C++

```c++
class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> result(n, 1);
        int prefixProduct = 1;
        for (int i = 0; i < n; i++) {
            result[i] *= prefixProduct;
            prefixProduct *= nums[i];
        }
        int suffixProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffixProduct;
            suffixProduct *= nums[i];
        }
        return result;
    }
};
```

## Py

```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]

        l = len(nums)

        for i in range(0, l - 1):
            left.append(left[-1] * nums[i])

        right = nums[-1]
        for i in range(l-2, -1, -1):
            left[i] *= right
            right *= nums[i]
            
        return left

```
