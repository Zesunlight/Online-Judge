# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 718. 最长重复子数组
Website: https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 5356 ms, 在所有 Python3 提交中击败了38.26%的用户
Memory Usage: 39.7 MB, 在所有 Python3 提交中击败了14.29%的用户
=================================================="""


class Solution:
    """
    给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
    """
    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        dp = [[0 for _ in range(len(A))] for _ in range(len(B))]
        for i in range(len(A)):
            if A[i] == B[0]:
                dp[0][i] = 1
        for i in range(1, len(B)):
            if A[0] == B[i]:
                dp[i][0] = 1
        for i in range(1, len(B)):
            for j in range(1, len(A)):
                if B[i] == A[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res

    def findLength_2(self, A: List[int], B: List[int]) -> int:
        # 令 dp[i][j] 表示 A[i:] 和 B[j:] 的最长公共前缀，那么答案即为所有 dp[i][j] 中的最大值。
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans
    """
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

'''
滑动窗口
我们可以枚举 A 和 B 所有的对齐方式。
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/
'''