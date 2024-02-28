# [2523. Closest Prime Numbers in Range](https://leetcode.com/problems/closest-prime-numbers-in-range/description/)

Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
num1 and num2 are both prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the minimum num1 value or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself.

```py
# class Solution:
#     def closestPrimes(self, l: int, n: int) -> List[int]:
#         if n <= 2:
#             return [-1, -1]

#         primes = [True] * (n+1)
#         primes[0] = primes[1] = False

#         for i in range(2, int(n**0.5) + 1):
#             if primes[i]:
#                 primes[i*i:n+1:i] = [False] * len(primes[i*i:n+1:i])

#         a = -1
#         b = -1
#         ans = [0,99999]

#         for i in range(l, n+1):
#             if primes[i]:
#                 b, a = i, b

#                 if ans[1] - ans[0] > b - a:
#                     ans = [a, b]

#         if a == -1:
#             return [-1,-1]

#         return ans

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n < 2: return False
            for x in range(2, int(n**0.5) + 1):
                if n % x == 0:
                    return False
            return True
        q = []
        diff = float('inf')
        pair = [-1,-1]
        for i in range(left,right+1):
            if isPrime(i): 
                q.append(i)
            while len(q)>=2:
                if abs(q[0]-q[1])<diff:
                    pair=[q[0],q[1]]
                    diff=abs(q[0]-q[1])  
                    if diff<=2: return pair
                q.pop(0)
        return pair
```
