"""
    Problem: 13. Roman to Integer
    Website: https://leetcode.com/problems/roman-to-integer/
    Difficulty: Easy
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 36 ms, faster than 95.95% of Python3 online submissions for Roman to Integer.
	Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
"""


class Solution:
	"""
	Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
	"""
    def romanToInt(self, s: str) -> int:
        res = 0
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s) - 1):
            if (s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')) or \
                (s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C')) or \
                (s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M')):
                res -= Roman[s[i]]
            else:
                res += Roman[s[i]]

        return res + Roman[s[-1]]
