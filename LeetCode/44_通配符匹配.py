"""
    Problem: 44. 通配符匹配
    Website: https://leetcode-cn.com/problems/wildcard-matching/
    Difficulty: Hard
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 1144 ms, faster than 25.78% of Python3 online submissions for Jump Game II.
    Memory Usage: 22.6 MB, less than 25.00% of Python3 online submissions for Jump Game II.
"""


class Solution:
    """
    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    """

    def isMatch(self, s: str, p: str) -> bool:
        match = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        match[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                match[0][i] = True
            else:
                break 
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    match[i][j] = match[i - 1][j - 1]
                elif p[j - 1] == '*':
                    match[i][j] = match[i][j - 1] or match[i - 1][j - 1] or match[i - 1][j]
                else:
                    match[i][j] = False
        return match[-1][-1]


    def isMatch_2(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
        return dp[m][n]
    """
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/wildcard-matching/solution/tong-pei-fu-pi-pei-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
