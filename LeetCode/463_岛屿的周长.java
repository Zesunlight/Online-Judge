import java.util.*;

/*
    463. 岛屿的周长
    https://leetcode-cn.com/problems/island-perimeter/

    给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
    网格中的格子水平和垂直方向相连（对角线方向不相连）。
    整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
    岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。
    网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

    执行用时：15 ms, 在所有 Java 提交中击败了6.79%的用户
    内存消耗：40.4 MB, 在所有 Java 提交中击败了5.05%的用户
 */


class Solution {
    public int islandPerimeter(int[][] grid) {
        int startX = -1, startY = -1;
        boolean find = false;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    startX = i;
                    startY = j;
                    find = true;
                    break;
                }
            }
            if (find) {
                break;
            }
        }
        return perimeter(grid, new boolean[grid.length][grid[0].length], startX, startY, 0);
    }

    public int perimeter(int[][] grid, boolean[][] visit, int x, int y, int len) {
        int focus = 0;
        if (visit[x][y]) {
            return focus;
        }
        visit[x][y] = true;

        if (x > 0) {
            if (grid[x-1][y] == 0) {
                focus++;
            } else {
                len += perimeter(grid, visit, x - 1, y, 0);
            }
        } else {
            focus++;
        }
        if (x < grid.length - 1) {
            if (grid[x+1][y] == 0) {
                focus++;
            } else {
                len += perimeter(grid, visit, x + 1, y, 0);
            }
        } else {
            focus++;
        }
        if (y > 0) {
            if (grid[x][y-1] == 0) {
                focus++;
            } else {
                len += perimeter(grid, visit, x, y - 1, 0);
            }
        } else {
            focus++;
        }
        if (y < grid[0].length - 1) {
            if (grid[x][y+1] == 0) {
                focus++;
            } else {
                len += perimeter(grid, visit, x, y + 1, 0);
            }
        } else {
            focus++;
        }

        return focus + len;
    }
}


class Solution2 {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public int islandPerimeter(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    int cnt = 0;
                    for (int k = 0; k < 4; ++k) {
                        int tx = i + dx[k];
                        int ty = j + dy[k];
                        if (tx < 0 || tx >= n || ty < 0 || ty >= m || grid[tx][ty] == 0) {
                            cnt += 1;
                        }
                    }
                    ans += cnt;
                }
            }
        }
        return ans;
    }
}


class Solution3 {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public int islandPerimeter(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    ans += dfs(i, j, grid, n, m);
                }
            }
        }
        return ans;
    }

    public int dfs(int x, int y, int[][] grid, int n, int m) {
        if (x < 0 || x >= n || y < 0 || y >= m || grid[x][y] == 0) {
            return 1;
        }
        if (grid[x][y] == 2) {
            return 0;
        }
        grid[x][y] = 2;
        int res = 0;
        for (int i = 0; i < 4; ++i) {
            int tx = x + dx[i];
            int ty = y + dy[i];
            res += dfs(tx, ty, grid, n, m);
        }
        return res;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/island-perimeter/solution/dao-yu-de-zhou-chang-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。