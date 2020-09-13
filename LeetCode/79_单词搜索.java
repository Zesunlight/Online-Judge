import java.util.*;

/*
    79. 单词搜索
    https://leetcode-cn.com/problems/word-search/

    给定一个二维网格和一个单词，找出该单词是否存在于网格中。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
    同一个单元格内的字母不允许被重复使用。

    执行用时：6 ms, 在所有 Java 提交中击败了92.07%的用户
    内存消耗：41.6 MB, 在所有 Java 提交中击败了77.54%的用户
 */


class Solution {
    boolean[][] visit;
    public boolean exist(char[][] board, String word) {
        int n = board.length, m = board[0].length;
        visit = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (exist(board, i, j, 0, word)) return true;
            }
        }
        return false;
    }

    public boolean exist(char[][] board, int x, int y, int start, String word) {
        if (board[x][y] != word.charAt(start) || visit[x][y]) return false;
        else {
            if (start == word.length() - 1) return true;
            visit[x][y] = true;
            if (x > 0 && exist(board, x - 1, y, start + 1, word)) return true;
            if (x < board.length - 1 && exist(board, x + 1, y, start + 1, word)) return true;
            if (y > 0 && exist(board, x, y - 1, start + 1, word)) return true;
            if (y < board[0].length - 1 && exist(board, x, y + 1, start + 1, word)) return true;
            visit[x][y] = false;
        }
        return false;
    }
}

