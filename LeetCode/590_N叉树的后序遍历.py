# -*- coding: UTF-8 -*-
"""=================================================
Problem: 590. N 叉树的后序遍历
Website: https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 56 ms
Memory Usage: 17.2 MB
=================================================="""
from typing import List

"""
给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        res = []
        if root is not None:
            for child in root.children:
                res.extend(self.postorder(child))
            res.append(root.val)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.postorder)
