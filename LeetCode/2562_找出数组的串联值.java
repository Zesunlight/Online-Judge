/*
    2562. 找出数组的串联值
    https://leetcode.cn/problems/find-the-array-concatenation-value/description

    给你一个下标从 0 开始的整数数组 nums 。
    现定义两个数字的 串联 是由这两个数值串联起来形成的新数字。

    例如，15 和 49 的串联是 1549 。
    nums 的 串联值 最初等于 0 。执行下述操作直到 nums 变为空：

    如果 nums 中存在不止一个数字，分别选中 nums 中的第一个元素和最后一个元素，
    将二者串联得到的值加到 nums 的 串联值 上，然后从 nums 中删除第一个和最后一个元素。
    如果仅存在一个元素，则将该元素的值加到 nums 的串联值上，然后删除这个元素。
    返回执行完所有操作后 nums 的串联值。

    执行用时：0 ms
    内存消耗：38.6 MB
 */


class Solution {
    public long findTheArrayConcVal(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int len = nums.length;

        long res = 0;
        for (int i = 0; i < len / 2; i++) {
            res += Long.parseLong(String.valueOf(nums[i]) + String.valueOf(nums[len - i - 1]));
        }
        if (len % 2 == 1) {
            res += nums[len / 2];
        }
        return res;
    }
}


public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.findTheArrayConcVal(new int[]{5,14,13,8,12}));
    }
}
