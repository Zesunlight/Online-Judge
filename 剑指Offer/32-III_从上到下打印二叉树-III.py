# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题32 - III. 从上到下打印二叉树 III
Website: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms, 在所有 Python3 提交中击败了80.96%的用户
Memory Usage: 14 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    请实现一个函数按照之字形顺序打印二叉树，
    即第一行按照从左到右的顺序打印，
    第二层按照从右到左的顺序打印，
    第三行再按照从左到右的顺序打印，其他行以此类推。
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []
        odd = True
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
            if not odd:
                temp.reverse()
            odd = not odd
            res.append(temp)
        return res

"""

"""
