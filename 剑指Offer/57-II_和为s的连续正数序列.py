# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题57 - II. 和为s的连续正数序列
Website: https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms, 在所有 Python3 提交中击败了99.61%的用户
Memory Usage: 13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

    序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
    """
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for i in range(2, target):
            temp = i * (i - 1) // 2
            if target <= temp:
                break
            if (target - temp) % i == 0:
                res.append([(target - temp) // i + j for j in range(i)])
        res.reverse()
        return res


    def findContinuousSequence_2(self, target: int) -> List[List[int]]:
        i = 1 # 滑动窗口的左边界
        j = 1 # 滑动窗口的右边界
        sum = 0 # 滑动窗口中数字的和
        res = []

        while i <= target // 2:
            if sum < target:
                # 右边界向右移动
                sum += j
                j += 1
            elif sum > target:
                # 左边界向右移动
                sum -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 左边界向右移动
                sum -= i
                i += 1

    return res
    """
    作者：nettee
    链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
