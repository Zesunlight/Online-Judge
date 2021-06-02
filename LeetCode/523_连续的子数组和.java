import java.util.*;

/*
    523. 连续的子数组和
    https://leetcode-cn.com/problems/continuous-subarray-sum/

    给你一个整数数组 nums 和一个整数k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
    子数组大小 至少为 2 ，且子数组元素总和为 k 的倍数。
    如果存在，返回 true ；否则，返回 false 。
    如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。

    执行用时：19 ms
    内存消耗：54.7 MB
 */


class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        int modSum = 0;
        for (int i = 0; i < nums.length; i++) {
            modSum = (modSum + nums[i]) % k;
            if (!map.containsKey(modSum)) {
                map.put(modSum, i);
            } else {
                if (i - map.get(modSum) >= 2) return true;
            }
        }
        return false;
    }
}
