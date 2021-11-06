/*
    268. 丢失的数字
    https://leetcode-cn.com/problems/missing-number/

    给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

    执行用时：0 ms
    内存消耗：38.7 MB
 */

class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        long sum = n * (n + 1) / 2;
        for (int i : nums) {
            sum -= i;
        }
        return (int) sum;
    }

    public int missingNumber2(int[] nums) {
        // https://leetcode-cn.com/problems/missing-number/solution/diu-shi-de-shu-zi-by-leetcode-solution-naow/
        int xor = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            xor ^= nums[i];
        }
        for (int i = 0; i <= n; i++) {
            xor ^= i;
        }
        return xor;
    }

}
public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.missingNumber(new int[] {9,6,4,2,3,5,7,0,1}));
    }
}
