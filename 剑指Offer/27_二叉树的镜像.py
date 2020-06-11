# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题27. 二叉树的镜像
Website: https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 28 ms, 在所有 Python3 提交中击败了99.22%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    请完成一个函数，输入一个二叉树，该函数输出它的镜像。
    """
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root


"""
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root

作者：jyd
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/solution/mian-shi-ti-27-er-cha-shu-de-jing-xiang-di-gui-fu-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
