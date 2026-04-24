# Brute force approach: O(m * n)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter = min(str1, str2, key=len)
        for i in range(len(shorter), 0, -1):
            candidate = shorter[:i]
            if candidate * (len(str1) // len(candidate)) == str1 and candidate * (len(str2) // len(candidate)) == str2:
                return candidate
        return ""


# Optimal approach: O(n) using math GCD
# If str1 + str2 == str2 + str1, a common divisor exists.
# String concatenation is only commutative when both strings share a repeating unit.
from math import gcd

class SolutionOptimal:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1), len(str2))]
        return ""
