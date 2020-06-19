# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题45. 把数组排成最小的数
Website: https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了21.66%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
    """
    class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0
        
        strs = [str(num) for num in nums]
        strs.sort(key = functools.cmp_to_key(sort_rule))
        return ''.join(strs)

"""
排序判断规则： 设 nums 任意两数字的字符串格式 x 和 y ，则
若拼接字符串 x + y > y + x ，则 m > n ；
反之，若 x + y < y + x ，则 n < m ；
根据以上规则，套用任何排序方法对 nums 执行排序即可。


作者：jyd
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

作者：jyd
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
