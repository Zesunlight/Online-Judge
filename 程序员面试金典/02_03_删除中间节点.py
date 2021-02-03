# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题 02.03. 删除中间节点
Website: https://leetcode-cn.com/problems/delete-middle-node-lcci/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了38%的用户
Memory Usage: 15.2 MB, 在所有 Python3 提交中击败了18%的用户
=================================================="""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。
    """
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next