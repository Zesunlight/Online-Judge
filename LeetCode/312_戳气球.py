# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 312. 戳气球
Website: https://leetcode-cn.com/problems/burst-balloons/
Difficulty: 困难
Author: 
Language: Python3
Result: Accepted
Runtime: 
Memory Usage: 
=================================================="""


class Solution:
    '''
    有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

    现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 
    这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

    求所能获得硬币的最大数量。
    '''

    class Solution:
        def maxCoins(self, nums: List[int]) -> int:
            n = len(nums)
            val = [1] + nums + [1]
            
            @lru_cache(None)
            def solve(left: int, right: int) -> int:
                if left >= right - 1:
                    return 0
                
                best = 0
                for i in range(left + 1, right):
                    total = val[left] * val[i] * val[right]
                    total += solve(left, i) + solve(i, right)
                    best = max(best, total)
                
                return best

            return solve(0, n + 1)


    class Solution_2:
        def maxCoins(self, nums: List[int]) -> int:
            n = len(nums)
            rec = [[0] * (n + 2) for _ in range(n + 2)]
            val = [1] + nums + [1]

            for i in range(n - 1, -1, -1):
                for j in range(i + 2, n + 2):
                    for k in range(i + 1, j):
                        total = val[i] * val[k] * val[j]
                        total += rec[i][k] + rec[k][j]
                        rec[i][j] = max(rec[i][j], total)
            
            return rec[0][n + 1]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/burst-balloons/solution/chuo-qi-qiu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
