# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题13. 机器人的运动范围
Website: https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了90.28%的用户
Memory Usage: 13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
    一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
    不能进入行坐标和列坐标的数位之和大于k的格子。
    例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
    但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
    """
    def movingCount(self, m: int, n: int, k: int) -> int:
        res = 0
        if k >= 9:
            for i in range(min(m, (k - 8) * 10 + 9)):
                for j in range(min(n, (k - 8) * 10 + 9)):
                    if i + j >= (k - 8) * 10 + 9:
                        break
                    if self.separate(i, j) <= k:
                        res += 1
        else:
            for i in range(min(m, 9)):
                for j in range(min(n, 9)):
                    if i + j <= k:
                        res += 1
        return res
    
    def separate(self, m, n):
        r = 0
        for c in str(m):
            r += int(c)
        for c in str(n):
            r += int(c)
        return r

"""
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
"""

"""
搜索的方向只需要朝下或朝右

def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/ji-qi-ren-de-yun-dong-fan-wei-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
