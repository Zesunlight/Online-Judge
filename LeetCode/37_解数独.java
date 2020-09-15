import java.util.*;

/*
    37. 解数独
    编写一个程序，通过已填充的空格来解决数独问题。

    编写一个程序，通过已填充的空格来解决数独问题。

    执行用时：7 ms, 在所有 Java 提交中击败了52.89%的用户
    内存消耗：37.4 MB, 在所有 Java 提交中击败了20.59%的用户
 */


class Solution {
    boolean finish = false;

    public void solveSudoku(char[][] board) {
        solveSudoku(board, 0, 0);
    }

    public void solveSudoku(char[][] board, int x, int y) {
        if (board[x][y] == '.') {
            for (char i = '1'; i <= '9'; i++) {
                if (check(board, x, y, i)) {
                    board[x][y] = i;
                    if (x == 8 && y == 8) finish = true;
                    if (y < 8) solveSudoku(board, x, y + 1);
                    else if (x < 8) solveSudoku(board, x + 1, 0);
                    if (finish) break;
                    board[x][y] = '.';
                }
            }
        } else {
            if (x == 8 && y == 8) {
                finish = true;
                return;
            }
            if (y < 8) solveSudoku(board, x, y + 1);
            else if (x < 8) solveSudoku(board, x + 1, 0);
        }
    }

    public boolean check(char[][] board, int x, int y, char value) {
        for (int i = 0; i < 9; i++) {
            if (board[i][y] == value) return false;
            if (board[x][i] == value) return false;
        }

        int groupX = x / 3, groupY = y / 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[groupX * 3 + i][groupY * 3 + j] == value) return false;
            }
        }

        return true;
    }
}


class LeetCode {
    public static void main(String[] args) {
        Solution s = new Solution();
        char[][] board = new char[][]{
                {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };
        s.solveSudoku(board);
        System.out.println(Arrays.deepToString(board));
    }
}