# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 5532. 奇偶树
Website: https://leetcode-cn.com/problems/even-odd-tree/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 552 ms
Memory Usage: 41.8 MB
=================================================="""


class Solution:
    """
    如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：

    二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
    偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
    奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
    给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。
    """
    def isEvenOddTree(self, root: TreeNode) -> bool:
        odd = False
        q = deque()
        q.append(root)
        while q:
            l = len(q)
            if odd:
                pre = 10 ** 6 + 1
            else:
                pre = 0
            for _ in range(l):
                top = q.popleft()
                if odd:
                    if top.val % 2 == 0 and top.val < pre:
                        pre = top.val
                    else:
                        return False
                else:
                    if top.val % 2 == 1 and top.val > pre:
                        pre = top.val
                    else:
                        return False
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            odd = not odd
        return True
