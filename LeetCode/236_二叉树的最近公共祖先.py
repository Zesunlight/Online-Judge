# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 236. 二叉树的最近公共祖先
Website: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 88 ms, 在所有 Python3 提交中击败了71.87%的用户
Memory Usage: 24 MB, 在所有 Python3 提交中击败了33.33%的用户
=================================================="""


class Solution:
    """
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is p or root is q:
            return root
        if root is None:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None:
            return right
        if right is None:
            return left
        return root


"""
if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root

作者：jyd
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
