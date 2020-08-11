import java.util.*;

/*
    130. 被围绕的区域
    https://leetcode-cn.com/problems/surrounded-regions/

    给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
    找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

    执行用时:9 ms, 在所有 Java 提交中击败了13.20%的用户
    内存消耗:41.6 MB, 在所所有 Java 提交中击败了91.43%的用户
 */


class Solution {
    int[][] visit;
    public void solve(char[][] board) {
        if (board.length <= 2 || board[0].length <= 2) return;
        int n = board.length, m = board[0].length;

        visit = new int[n][m];
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (board[i][0] == 'O') {
                queue.add(new int[] {i, 0});
            }
            if (board[i][m - 1] == 'O') {
                queue.add(new int[] {i, m - 1});
            }
        }
        for (int i = 1; i < m - 1; i++) {
            if (board[0][i] == 'O') {
                queue.add(new int[] {0, i});
            }
            if (board[n - 1][i] == 'O') {
                queue.add(new int[] {n - 1, i});
            }
        }

        while (!queue.isEmpty()) {
            int[] start = queue.poll();
            visit[start[0]][start[1]] = 1;
            if (start[0] - 1 >= 0 && board[start[0] - 1][start[1]] == 'O' && visit[start[0] - 1][start[1]] == 0) queue.offer(new int[] {start[0] - 1, start[1]});
            if (start[0] + 1 < n && board[start[0] + 1][start[1]] == 'O' && visit[start[0] + 1][start[1]] == 0) queue.offer(new int[] {start[0] + 1, start[1]});
            if (start[1] - 1 >= 0 && board[start[0]][start[1] - 1] == 'O' && visit[start[0]][start[1] - 1] == 0) queue.offer(new int[] {start[0], start[1] - 1});
            if (start[1] + 1 < m && board[start[0]][start[1] + 1] == 'O' && visit[start[0]][start[1] + 1] == 0) queue.offer(new int[] {start[0], start[1] + 1});
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'O' && visit[i][j] == 0) board[i][j] = 'X';
            }
        }
    }
}


class Solution2 {
    int[] dx = {1, -1, 0, 0};
    int[] dy = {0, 0, 1, -1};

    public void solve(char[][] board) {
        int n = board.length;
        if (n == 0) {
            return;
        }
        int m = board[0].length;
        Queue<int[]> queue = new LinkedList<int[]>();
        for (int i = 0; i < n; i++) {
            if (board[i][0] == 'O') {
                queue.offer(new int[]{i, 0});
            }
            if (board[i][m - 1] == 'O') {
                queue.offer(new int[]{i, m - 1});
            }
        }
        for (int i = 1; i < m - 1; i++) {
            if (board[0][i] == 'O') {
                queue.offer(new int[]{0, i});
            }
            if (board[n - 1][i] == 'O') {
                queue.offer(new int[]{n - 1, i});
            }
        }
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int x = cell[0], y = cell[1];
            board[x][y] = 'A';
            for (int i = 0; i < 4; i++) {
                int mx = x + dx[i], my = y + dy[i];
                if (mx < 0 || my < 0 || mx >= n || my >= m || board[mx][my] != 'O') {
                    continue;
                }
                queue.offer(new int[]{mx, my});
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'A') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/surrounded-regions/solution/bei-wei-rao-de-qu-yu-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    int n, m;

    public void solve(char[][] board) {
        n = board.length;
        if (n == 0) {
            return;
        }
        m = board[0].length;
        for (int i = 0; i < n; i++) {
            dfs(board, i, 0);
            dfs(board, i, m - 1);
        }
        for (int i = 1; i < m - 1; i++) {
            dfs(board, 0, i);
            dfs(board, n - 1, i);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'A') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }

    public void dfs(char[][] board, int x, int y) {
        if (x < 0 || x >= n || y < 0 || y >= m || board[x][y] != 'O') {
            return;
        }
        board[x][y] = 'A';
        dfs(board, x + 1, y);
        dfs(board, x - 1, y);
        dfs(board, x, y + 1);
        dfs(board, x, y - 1);
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/surrounded-regions/solution/bei-wei-rao-de-qu-yu-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。