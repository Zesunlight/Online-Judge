import java.util.*;

/*
    面试题 08.03. 魔术索引
    https://leetcode-cn.com/problems/magic-index-lcci/

    魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。
    给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。
    若有多个魔术索引，返回索引值最小的一个。

    执行用时：1 ms, 在所有 Java 提交中击败了47.45%的用户
    内存消耗：40.7 MB, 在所有 Java 提交中击败了45.45%的用户
 */


class Solution {
    public int findMagicIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (i == nums[i]) return i;
        }
        return -1;
    }
}

/*
def findMagicIndex(self, nums: List[int]) -> int:
    i=0
    while i < len(nums):
        if i==nums[i]:
            return i
        if i<nums[i]:
            i=nums[i]
        else:
            i+=1
    return -1
*/