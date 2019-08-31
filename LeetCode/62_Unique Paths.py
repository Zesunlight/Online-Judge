"""
    Problem: 62. Unique Paths
    Website: https://leetcode.com/problems/unique-paths/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 36 ms, faster than 75.74% of Python3 online submissions for Unique Paths.
    Memory Usage: 14 MB, less than 5.77% of Python3 online submissions for Unique Paths.
"""


class Solution:
    """
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time.
    The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    How many possible unique paths are there?
    """

    def uniquePaths(self, m: int, n: int) -> int:
        """
        from scipy.special import comb
        print(int(comb(m + n - 2, min(m, n) - 1)))

        Runtime: 132 ms, faster than 5.92% of Python3 online submissions for Unique Paths.
        Memory Usage: 36.1 MB, less than 5.77% of Python3 online submissions for Unique Paths.
        """

        n, m = m + n - 2, min(m, n) - 1
        if n < 0 or m < 0:
            return 0

        r = 1
        for i in range(1, m + 1):
            r = r * (n - m + i) / i

        return r


s = Solution()
print(s.uniquePaths(7, 3))

"""
https://leetcode.com/problems/unique-paths/discuss/22953/Java-DP-solution-with-complexity-O(n*m)

public class Solution {
    public int uniquePaths(int m, int n) {
        Integer[][] map = new Integer[m][n];
        for(int i = 0; i<m;i++){
            map[i][0] = 1;
        }
        for(int j= 0;j<n;j++){
            map[0][j]=1;
        }
        for(int i = 1;i<m;i++){
            for(int j = 1;j<n;j++){
                map[i][j] = map[i-1][j]+map[i][j-1];
            }
        }
        return map[m-1][n-1];
    }
}
"""