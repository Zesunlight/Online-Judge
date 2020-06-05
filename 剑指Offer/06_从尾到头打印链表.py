# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题06. 从尾到头打印链表
Website: https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了70.67%的用户
Memory Usage: 15.4 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
    """
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

"""
可用栈实现
"""
