# [204. Count Primes](https://leetcode.com/problems/count-primes/description/)

Given an integer n, return the number of prime numbers that are strictly less than n.

```py
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        
    
        return sum(primes)
```
