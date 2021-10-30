/*
    258. 各位相加
    https://leetcode-cn.com/problems/add-digits/submissions/

    给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

    执行用时：0 ms
    内存消耗：35.6 MB
 */

class Solution {
    public int addDigits(int num) {
        if (num == 0) {
            return 0;
        }
        int res = num % 9;
        if (res == 0) {
            return 9;
        }
        return res;
    }

    public int addDigits2(int num) {
        return (num - 1) % 9 + 1;
    }
}


public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.addDigits(38));
    }
}
