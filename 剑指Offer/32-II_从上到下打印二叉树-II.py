# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题32 - II. 从上到下打印二叉树 II
Website: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms, 在所有 Python3 提交中击败了81.08%的用户
Memory Usage: 13.8 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
    """
    if root is None:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            temp = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                temp.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(temp)
        return res

"""

"""
