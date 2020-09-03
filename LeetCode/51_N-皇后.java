import java.util.*;

/*
    51. N 皇后
    https://leetcode-cn.com/problems/n-queens/

    n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
    每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

    执行用时：7 ms, 在所有 Java 提交中击败了34.57%的用户
    内存消耗：40.7 MB, 在所有 Java 提交中击败了7.57%的用户
 */


class Solution {
    List<List<String>> scheme = new ArrayList<>();
    Set<Integer> row = new HashSet<>(), col = new HashSet<>(), diag = new HashSet<>(), diagR = new HashSet<>();

    public List<List<String>> solveNQueens(int n) {
        char[][] initial = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                initial[i][j] = '.';
            }
        }
        exact(0, initial);
        return scheme;
    }

    public void exact(int start, char[][] cur) {
        if (start >= cur.length) {
            List<String> r = new ArrayList<>();
            for (int i = 0; i < start; i++) {
                r.add(new String(cur[i]));
            }
            scheme.add(r);
        }

        for (int i = 0; i < cur.length; i++) {
            if (row.contains(start)) continue;
            if (col.contains(i)) continue;
            if (diag.contains(i - start)) continue;
            if (diagR.contains(i + start)) continue;

            row.add(start);
            col.add(i);
            diag.add(i - start);
            diagR.add(i + start);

            cur[start][i] = 'Q';
            exact(start + 1, cur);
            cur[start][i] = '.';

            row.remove(start);
            col.remove(i);
            diag.remove(i - start);
            diagR.remove(i + start);
        }
    }
}
