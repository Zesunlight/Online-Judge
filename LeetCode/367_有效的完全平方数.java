/*
    367. 有效的完全平方数
    https://leetcode-cn.com/problems/valid-perfect-square/

    给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

    执行用时：0 ms
    内存消耗：35.2 MB
 */

class Solution {
    public boolean isPerfectSquare(int num) {
        int q = (int) Math.floor(Math.sqrt(num));
        if (q * q == num) {
            return true;
        }
        return false;
    }

    // https://leetcode-cn.com/problems/valid-perfect-square/solution/you-xiao-de-wan-quan-ping-fang-shu-by-le-wkee/
    // def isPerfectSquare(self, num: int) -> bool:
    //     return float.is_integer(pow(num, 0.5))

    public boolean isPerfectSquare2(int num) {
        // https://leetcode-cn.com/problems/valid-perfect-square/solution/you-xiao-de-wan-quan-ping-fang-shu-by-le-wkee/
        int left = 0, right = num;
        while (left <= right) {
            int mid = (right - left) / 2 + left;
            long square = (long) mid * mid;
            if (square < num) {
                left = mid + 1;
            } else if (square > num) {
                right = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
  
    // 牛顿迭代
    
}


public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.isPerfectSquare(4));
    }
}
