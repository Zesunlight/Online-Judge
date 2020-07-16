/*
    12. 矩阵中的路径
    https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/

    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
    如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。

    执行用时：10 ms, 在所有 Java 提交中击败了17.00%的用户
    内存消耗：41.5 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class Solution {
    public boolean exist(char[][] board, String word) {
        int[][] visit = new int[board.length][board[0].length];
        for (int i = 0; i < board.length; ++i) {
            for (int j = 0; j < board[0].length; ++j) {
                if (dfs(board, visit, word, i, j)) return true;
            }
        }
        return false;
    }

    public boolean dfs(char[][] board, int[][] visit, String word, int x, int y) {
        if (board[x][y] == word.charAt(0) && visit[x][y] != 1) {
            visit[x][y] = 1;
            String temp = word.substring(1);
            if (temp.equals("")) return true;

            if (x > 0) {
                if (dfs(board, visit, temp, x - 1, y)) return true;
            }
            if (x < board.length - 1) {
                if (dfs(board, visit, temp, x + 1, y)) return true;
            }
            if (y > 0) {
                if (dfs(board, visit, temp, x, y - 1)) return true;
            }
            if (y < board[0].length - 1) {
                if (dfs(board, visit, temp, x, y + 1)) return true;
            }

            visit[x][y] = 0;
        }

        return false;
    }
}

class Solution2 {
    public boolean exist(char[][] board, String word) {
        char[] words = word.toCharArray();
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[0].length; j++) {
                if(dfs(board, words, i, j, 0)) return true;
            }
        }
        return false;
    }
    boolean dfs(char[][] board, char[] word, int i, int j, int k) {
        if(i >= board.length || i < 0 || j >= board[0].length || j < 0 || board[i][j] != word[k]) return false;
        if(k == word.length - 1) return true;
        char tmp = board[i][j];
        board[i][j] = '/';
        boolean res = dfs(board, word, i + 1, j, k + 1) || dfs(board, word, i - 1, j, k + 1) || 
                      dfs(board, word, i, j + 1, k + 1) || dfs(board, word, i , j - 1, k + 1);
        board[i][j] = tmp;
        return res;
    }
}

// 作者：jyd
// 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。