"""
    Problem: 63. 不同路径 II
    Website: https://leetcode-cn.com/problems/unique-paths-ii/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 40 ms, faster than 82.00% of Python3 online submissions for Minimum Path Sum.
    Memory Usage: 13.5 MB, less than 14.29% of Python3 online submissions for Minimum Path Sum.
"""


class Solution:
    """
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        arrive = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        arrive[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    if i > 0:
                        arrive[i][j] += arrive[i - 1][j]
                    if j > 0:
                        arrive[i][j] += arrive[i][j - 1]
        return arrive[-1][-1]


"""
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int n = obstacleGrid.length, m = obstacleGrid[0].length;
        int[] f = new int[m];  # 滚动数组优化空间

        f[0] = obstacleGrid[0][0] == 0 ? 1 : 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (obstacleGrid[i][j] == 1) {
                    f[j] = 0;
                    continue;
                }
                if (j - 1 >= 0 && obstacleGrid[i][j - 1] == 0) {
                    f[j] += f[j - 1];
                }
            }
        }
        
        return f[m - 1];
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/unique-paths-ii/solution/bu-tong-lu-jing-ii-by-leetcode-solution-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""