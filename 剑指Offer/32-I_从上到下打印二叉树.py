# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题32 - I. 从上到下打印二叉树
Website: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了35.63%的用户
Memory Usage: 13.9 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
    """
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return res

"""

"""
