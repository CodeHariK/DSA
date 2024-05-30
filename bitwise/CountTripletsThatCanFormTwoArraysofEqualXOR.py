# [1442. Count Triplets That Can Form Two Arrays of Equal XOR](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor)

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        ans = 0
        for i in range(len(arr)):
            a = arr[i]
            for k in range(i+1, len(arr)):
                a ^= arr[k]
                if a == 0:
                    ans += k - i

        return ans
