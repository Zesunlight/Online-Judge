# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1365. 有多少小于当前数字的数字
Website: https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms, 在所有 Python3 提交中击败了99.27%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了5.35%的用户
=================================================="""


class Solution:
    """
    给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
    换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
    以数组形式返回答案。
    """    
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        res = {s[0]: 0}
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                res[s[i]] = i
        for i in range(len(nums)):
            nums[i] = res[nums[i]]
        return nums

'''
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] cnt = new int[101];
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            cnt[nums[i]]++;
        }
        for (int i = 1; i <= 100; i++) {
            cnt[i] += cnt[i - 1];
        }
        int[] ret = new int[n];
        for (int i = 0; i < n; i++) {
            ret[i] = nums[i] == 0 ? 0 : cnt[nums[i] - 1];
        }
        return ret;
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/solution/you-duo-shao-xiao-yu-dang-qian-shu-zi-de-shu-zi--2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''