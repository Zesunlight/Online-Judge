# -*- coding: UTF-8 -*-
"""=================================================
Problem: 516. 最长回文子序列
Website: https://leetcode-cn.com/problems/longest-palindromic-subsequence/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 2416 ms
Memory Usage: 31。8 MB
=================================================="""


"""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        m = 1
        palindrome = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            palindrome[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrome[i][i + 1] = 2
                m = 2
            else:
                palindrome[i][i + 1] = 1

        for step in range(2, n):
            for i in range(n - step):
                if s[i] == s[i + step]:
                    palindrome[i][i + step] = 2 + palindrome[i + 1][i + step - 1]
                else:
                    palindrome[i][i + step] = max(palindrome[i + 1][i + step],
                                                  palindrome[i][i + step - 1])
                m = max(m, palindrome[i][i + step])
        return m

    def longestPalindromeSubseq2(self, s: str) -> int:
        # https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/zui-chang-hui-wen-zi-xu-lie-by-leetcode-hcjqp/
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindromeSubseq('aa'))
