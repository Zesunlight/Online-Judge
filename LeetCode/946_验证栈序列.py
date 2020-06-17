# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 946. 验证栈序列
Website: https://leetcode-cn.com/problems/validate-stack-sequences/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 88 ms, 在所有 Python3 提交中击败了78.60%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了25.00%的用户
=================================================="""


class Solution:
    """
    给定 pushed 和 popped 两个序列，每个序列中的值都不重复，
    只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，
    返回 true；否则，返回 false 。
    """
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) <= 2:
            return True
        stack = []
        for i in range(len(popped)):
            while not stack or stack[-1] != popped[i]:
                if not pushed:
                    return False
                stack.append(pushed.pop(0))
            else:
                stack.pop()
        return True
