import java.util.*;

/*
    64. 最小路径和
    https://leetcode-cn.com/problems/minimum-path-sum/

    https://leetcode-cn.com/problems/minimum-path-sum/

    执行用时：2 ms, 在所有 Java 提交中击败了98.20%的用户
    内存消耗：42.9 MB, 在所有 Java 提交中击败了22.72%的用户
 */



class Solution {
    public int minPathSum(int[][] grid) {
        int[] dp = new int[grid[0].length];
        dp[0] = grid[0][0];
        for (int i = 1; i < grid[0].length; ++i) {
            dp[i] = dp[i - 1] + grid[0][i];
        }
        for (int i = 1; i < grid.length; ++i) {
            for (int j = 0; j < grid[0].length; ++j) {
                if (j == 0) {
                    dp[j] = dp[j] + grid[i][j];
                } else {
                    dp[j] = Math.min(dp[j - 1], dp[j]) + grid[i][j];
                }
            }
        }
        return dp[grid[0].length - 1];
    }
}

