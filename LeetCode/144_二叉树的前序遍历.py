# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 144. 二叉树的前序遍历
Website: https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms, 在所有 Python3 提交中击败了66.28%的用户
Memory Usage: 13.5 MB, 在所有 Python3 提交中击败了7.14%的用户
=================================================="""


class Solution:
    """
    给定一个二叉树，返回它的 前序 遍历。
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            res.append(root.val)
            res.extend(self.preorderTraversal(root.left))
            res.extend(self.preorderTraversal(root.right))
        return res

"""
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []
        
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return output

作者：LeetCode
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""