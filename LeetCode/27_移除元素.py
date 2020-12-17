# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 27. 移除元素
Website: https://leetcode-cn.com/problems/remove-element/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms
Memory Usage: 14.9 MB
=================================================="""


from typing import List


class Solution:
    '''
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
    不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
    '''
    
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        t = len(nums) - j
        for _ in range(t):
            nums.pop(-1)

        return j


'''
public int removeElement(int[] nums, int val) {
    int i = 0;
    int n = nums.length;
    while (i < n) {
        if (nums[i] == val) {
            nums[i] = nums[n - 1];
            // reduce array size by one
            n--;
        } else {
            i++;
        }
    }
    return n;
}

作者：LeetCode
链接：https://leetcode-cn.com/problems/remove-element/solution/yi-chu-yuan-su-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
