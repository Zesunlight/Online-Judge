# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 98. 验证二叉搜索树
Website: https://leetcode-cn.com/problems/validate-binary-search-tree/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 56 ms, 在所有 Python3 提交中击败了72.37%的用户
Memory Usage: 15.9 MB, 在所有 Python3 提交中击败了9.52%的用户
=================================================="""


class Solution:
    """
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。

    假设一个二叉搜索树具有如下特征：

    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
    """
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.helper(root.left, -1<<32, root.val) and self.helper(root.right, root.val, 1<<32)
    
    def helper(self, node, inf, sup):
        if node is None:
            return True
        if inf < node.val < sup:
            return self.helper(node.left, inf, node.val) and self.helper(node.right, node.val, sup)
        else:
            return False

"""
二叉搜索树「中序遍历」得到的值构成的序列一定是升序的，
这启示我们在中序遍历的时候实时检查当前节点的值是否大于前一个中序遍历到的节点的值即可。
如果均大于说明这个序列是升序的，整棵树是二叉搜索树，否则不是

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

"""
class Solution {
    long pre = Long.MIN_VALUE;
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        // 访问左子树
        if (!isValidBST(root.left)) {
            return false;
        }
        // 访问当前节点：如果当前节点小于等于中序遍历的前一个节点，说明不满足BST，返回 false；否则继续遍历。
        if (root.val <= pre) {
            return false;
        }
        pre = root.val;
        // 访问右子树
        return isValidBST(root.right);
    }
}

作者：sweetiee
链接：https://leetcode-cn.com/problems/validate-binary-search-tree/solution/zhong-xu-bian-li-qing-song-na-xia-bi-xu-miao-dong-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""