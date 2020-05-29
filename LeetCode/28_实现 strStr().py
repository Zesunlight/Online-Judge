# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 28. 实现 strStr()
Website: https://leetcode-cn.com/problems/implement-strstr/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms, 在所有 Python3 提交中击败了84.98%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了9.09%的用户
=================================================="""


class Solution:
    """
    实现 strStr() 函数。

    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

    当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

    对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None:
            return -1
        total = len(haystack)
        goal = len(needle)
        if goal == 0:
            return 0
        if total == goal:
            return 0 if haystack == needle else -1
        elif total < goal:
            return -1
        for i in range(total - goal + 1):
            if needle == haystack[i:i+goal]:
                return i
        return -1


"""
return haystack.find(needle)


https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode/
def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

双指针 - 线性时间复杂度

Rabin Karp - 常数复杂度
滚动哈希：常数时间生成哈希码
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L > n:
            return -1
        
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**31
        
        # lambda-function to convert character to integer
        h_to_int = lambda i : ord(haystack[i]) - ord('a')
        needle_to_int = lambda i : ord(needle[i]) - ord('a')
        
        # compute the hash of strings haystack[:L], needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h:
            return 0
              
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus) 
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start

        return -1
"""