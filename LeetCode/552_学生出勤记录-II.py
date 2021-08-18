# -*- coding: UTF-8 -*-
"""=================================================
Problem: 552. 学生出勤记录 II
Website: https://leetcode-cn.com/problems/student-attendance-record-ii/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 7868 ms
Memory Usage: 66.6 MB
=================================================="""
from typing import List

"""
可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。
记录中只含下面三种字符：
'A'：Absent，缺勤
'L'：Late，迟到
'P'：Present，到场
如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

按 总出勤 计，学生缺勤（'A'）严格 少于两天。
学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。
答案可能很大，所以返回对 109 + 7 取余 的结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/student-attendance-record-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[0, 0] for _ in range(3)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        mod = int(1e9 + 7)

        for i in range(1, n + 1):
            # present
            for a in range(2):
                for l in range(3):
                    dp[i][0][a] += dp[i - 1][l][a]

            # late
            for a in range(2):
                dp[i][1][a] += dp[i - 1][0][a]
                dp[i][2][a] += dp[i - 1][1][a]

            # absent
            dp[i][0][1] += sum(dp[i - 1][l][0] for l in range(3))

            for a in range(2):
                for l in range(3):
                    dp[i][l][a] %= mod

        return sum(map(sum, dp[n])) % mod

    def checkRecord2(self, n: int) -> int:
        # https://leetcode-cn.com/problems/student-attendance-record-ii/solution/xue-sheng-chu-qin-ji-lu-ii-by-leetcode-s-kdlm/
        # 矩阵快速幂
        MOD = 10 ** 9 + 7
        mat = [
            [1, 1, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0],
        ]

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            rows, columns, temp = len(a), len(b[0]), len(b)
            c = [[0] * columns for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    for k in range(temp):
                        c[i][j] += a[i][k] * b[k][j]
                        c[i][j] %= MOD
            return c

        def matrixPow(mat: List[List[int]], n: int) -> List[List[int]]:
            ret = [[1, 0, 0, 0, 0, 0]]
            while n > 0:
                if (n & 1) == 1:
                    ret = multiply(ret, mat)
                n >>= 1
                mat = multiply(mat, mat)
            return ret

        res = matrixPow(mat, n)
        ans = sum(res[0])
        return ans % MOD


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkRecord(4))  # 43
