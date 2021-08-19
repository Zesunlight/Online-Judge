# -*- coding: UTF-8 -*-
"""=================================================
Problem: 345. 反转字符串中的元音字母
Website: https://leetcode-cn.com/problems/reverse-vowels-of-a-string/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms
Memory Usage: 18.9 MB
=================================================="""

"""
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = []
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                vowel.append((i, s[i]))
        n = len(vowel)
        for i in range(n):
            s[vowel[i][0]] = vowel[n - i - 1][1]
        return ''.join(s)

    def reverseVowels2(self, s: str) -> str:
        # 双指针
        # https://leetcode-cn.com/problems/reverse-vowels-of-a-string/solution/fan-zhuan-zi-fu-chuan-zhong-de-yuan-yin-2bmos/
        def isVowel(ch: str) -> bool:
            return ch in "aeiouAEIOU"

        n = len(s)
        s = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and not isVowel(s[i]):
                i += 1
            while j > 0 and not isVowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseVowels("leetcode"))
