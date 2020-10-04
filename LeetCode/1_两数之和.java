/*
    1. 两数之和
    https://leetcode-cn.com/problems/two-sum/

    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

    执行用时：2 ms, 在所有 Java 提交中击败了99.58%的用户
    内存消耗：39 MB, 在所有 Java 提交中击败了65.32%的用户
 */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int couple = target - nums[i];
            if (map.containsKey(couple)) {
                return new int[] {map.get(couple), i};
            } else {
                map.put(nums[i], i);
            }
        }
        return new int[0];
    }
}