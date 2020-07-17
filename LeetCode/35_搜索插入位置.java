import java.util.*;

/*
    35. 搜索插入位置
    https://leetcode-cn.com/problems/search-insert-position/

    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
    如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    你可以假设数组中无重复元素。

    执行用时：0 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：39.3 MB, 在所有 Java 提交中击败了5.55%的用户
 */


class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target){
                right = mid - 1;
            } else {
                return mid;
            }
        }
        return left;
    }
}

