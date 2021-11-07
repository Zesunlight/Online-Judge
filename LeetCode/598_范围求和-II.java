/*
    598. 范围求和 II
    https://leetcode-cn.com/problems/range-addition-ii/

    给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。
    操作用二维数组表示，其中的每个操作用一个含有两个正整数 a 和 b 的数组表示，
    含义是将所有符合 0 <= i < a 以及 0 <= j < b 的元素 M[i][j] 的值都增加 1。
    在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。

    执行用时：0 ms
    内存消耗：38.5 MB
 */

class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        int l = m;
        int r = n;
        for (int[] op : ops) {
            l = Math.min(op[0], l);
            r = Math.min(op[1], r);
        }
        return l * r;
    }
}
public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.maxCount(3, 3, new int[][] {{2, 2}, {3, 3}}));
    }
}
