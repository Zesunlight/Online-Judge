import java.util.*;

/*
    329. 矩阵中的最长递增路径
    https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/

    给给定一个整数矩阵，找出最长递增路径的长度。

    对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

    执行用时：8 ms, 在所有 Java 提交中击败了98.64%的用户
    内存消耗：39.7 MB, 在所有 Java 提交中击败了42.86%的用户
 */


class Solution {
    int[][] riddle, visit;
    int row, col;

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null) return 0;

        riddle = matrix;
        row = matrix.length;
        if (row == 0) return 0;
        col = matrix[0].length;
        if (col == 0) return 0;
        visit = new int[row][col];

        int res = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                res = Math.max(res, pathFromPoint(i, j));
            }
        }
        return res;
    }

    public int pathFromPoint(int x, int y) {
        if (visit[x][y] != 0) return visit[x][y];

        int temp = 0;
        if (x - 1 >= 0 && riddle[x - 1][y] > riddle[x][y]) {
            temp = Math.max(pathFromPoint(x - 1, y), temp);
        }
        if (x + 1 < row && riddle[x + 1][y] > riddle[x][y]) {
            temp = Math.max(pathFromPoint(x + 1, y), temp);
        }
        if (y - 1 >= 0 && riddle[x][y - 1] > riddle[x][y]) {
            temp = Math.max(pathFromPoint(x, y - 1), temp);
        }
        if (y + 1 < col && riddle[x][y + 1] > riddle[x][y]) {
            temp = Math.max(pathFromPoint(x, y + 1), temp);
        }

        visit[x][y] = 1 + temp;
        return 1 + temp;
    }
}


class Solution {
    public int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public int rows, columns;

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        rows = matrix.length;
        columns = matrix[0].length;
        int[][] memo = new int[rows][columns];
        int ans = 0;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < columns; ++j) {
                ans = Math.max(ans, dfs(matrix, i, j, memo));
            }
        }
        return ans;
    }

    public int dfs(int[][] matrix, int row, int column, int[][] memo) {
        if (memo[row][column] != 0) {
            return memo[row][column];
        }
        ++memo[row][column];
        for (int[] dir : dirs) {
            int newRow = row + dir[0], newColumn = column + dir[1];
            if (newRow >= 0 && newRow < rows && newColumn >= 0 && newColumn < columns && matrix[newRow][newColumn] > matrix[row][column]) {
                memo[row][column] = Math.max(memo[row][column], dfs(matrix, newRow, newColumn, memo) + 1);
            }
        }
        return memo[row][column];
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/solution/ju-zhen-zhong-de-zui-chang-di-zeng-lu-jing-by-le-2/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。