/*=================================================
Problem: 面试题 51. 数组中的逆序对
Website: https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
Difficulty: 困难
Author: ZYZ
Language: Java
Result: Accepted
执行用时：42 ms, 在所有 Java 提交中击败了25.93%的用户
内存消耗：48.1 MB, 在所有 Java 提交中击败了100.00%的用户
==================================================*/


class Solution {
    int res = 0;

    public int reversePairs(int[] nums) {
        if (nums.length <= 1) return 0;
        half(nums);
        return res;
    }

    public int[] half(int[] nums) {
        if (nums.length <= 1) return nums;
        int[] left = half(Arrays.copyOfRange(nums, 0, nums.length / 2));
        int[] right = half(Arrays.copyOfRange(nums, nums.length / 2, nums.length));
        int[] merge = new int[nums.length];
        int k = 0, i = 0, j = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                merge[k] = left[i];
                ++i;
            } else {
                res += left.length - i;
                merge[k] = right[j];
                ++j;
            }
            ++k;
        }
        while (i < left.length) {
            merge[k] = left[i];
            ++i;
            ++k;
        }
        while (j < right.length) {
            merge[k] = right[j];
            ++j;
            ++k;
        }
        return merge;
    }
}