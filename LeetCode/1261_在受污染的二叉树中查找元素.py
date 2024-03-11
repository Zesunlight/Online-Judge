# -*- coding: UTF-8 -*-
"""=================================================
Problem: 1261. 在受污染的二叉树中查找元素
Website: https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/description/?envType=daily-question&envId=2024-03-12
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 1448 ms
Memory Usage: 20.73 MB
=================================================="""
from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.restore(root, 0)
        self.root = root

    def restore(self, node: TreeNode, value: int):
        if node:
            node.val = value
            self.restore(node.left, 2 * value + 1)
            self.restore(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        return self.exist(self.root, target)

    def exist(self, node: TreeNode, target: int) -> bool:
        if node:
            if node.val == target:
                return True
            if target <= node.val * 2:
                return False
            return self.exist(node.left, target) or self.exist(node.right, target)
        else:
            return False


class FindElements2:
    # https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/solutions/2674238/zai-shou-wu-ran-de-er-cha-shu-zhong-cha-5l56x/
    def __init__(self, root: Optional[TreeNode]):
        self.valSet = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.valSet

    def dfs(self, node: TreeNode, val: int):
        if node is None:
            return
        node.val = val
        self.valSet.add(val)
        self.dfs(node.left, val * 2 + 1)
        self.dfs(node.right, val * 2 + 2)
