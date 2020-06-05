# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题11. 旋转数组的最小数字
Website: https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了30.45%的用户
Memory Usage: 13.9 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
    例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
    """
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) == 1:
            return numbers[0]
        if numbers[0] < numbers[-1]:
            return numbers[0]
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] >= numbers[left]:
                left = mid + 1
            else:
                right = mid
                break
        while (right - 1) >= 0 and numbers[right - 1] <= numbers[right]:
            right -= 1
        return numbers[right]


"""
class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]

作者：jyd
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
