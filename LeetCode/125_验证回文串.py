# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 125. 验证回文串
Website: https://leetcode-cn.com/problems/valid-palindrome/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 56 ms, 在所有 Python3 提交中击败了71.20%的用户
Memory Usage: 14.3 MB, 在所有 Python3 提交中击败了37.04%的用户
=================================================="""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        if not s:
            return True
        ss = ''.join(re.findall(r'\w', s)).lower()
        return ss == ss[::-1]


class Solution_2:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]
"""
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/valid-palindrome/solution/yan-zheng-hui-wen-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution_3:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1

        return True
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/valid-palindrome/solution/yan-zheng-hui-wen-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

