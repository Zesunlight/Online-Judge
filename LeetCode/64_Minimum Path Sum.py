"""
    Problem: 64. Minimum Path Sum
    Website: https://leetcode.com/problems/minimum-path-sum/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 108 ms, faster than 90.33% of Python3 online submissions for Minimum Path Sum.
    Memory Usage: 15.5 MB, less than 17.54% of Python3 online submissions for Minimum Path Sum.
"""


class Solution:
    """
    Given a m x n grid filled with non-negative numbers,
    find a path from top left to bottom right which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.
    """

    def minPathSum(self, grid) -> int:
        # 其实并不需要额外的数组
        dp = [[0 for _ in range(len(grid[0]))] for j in range(len(grid))]

        dp[-1][-1] = grid[-1][-1]
        for i in range(len(dp) - 2, -1, -1):
            dp[i][-1] = dp[i + 1][-1] + grid[i][-1]
        for j in range(len(dp[0]) - 2, -1, -1):
            dp[-1][j] = dp[-1][j + 1] + grid[-1][j]

        for i in range(len(dp) - 2, -1, -1):
            for j in range(len(dp[0]) - 2, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]

        return dp[0][0]


s = Solution()
a = [
    [1, 3, 1, 2],
    [1, 5, 1, 6],
    [4, 2, 1, 1]
    ]
a = [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(a))


"""
https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms

def minPathSum(self, grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]
"""