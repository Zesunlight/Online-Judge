# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 101. 对称二叉树
Website: https://leetcode-cn.com/problems/symmetric-tree/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms, 在所有 Python3 提交中击败了69.37%的用户
Memory Usage: 13.9 MB, 在所有 Python3 提交中击败了6.06%的用户
=================================================="""


class Solution:
    """
    给定一个二叉树，检查它是否是镜像对称的。
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        layer = []
        
        while queue:
            next_q = []
            for node in queue:
                if node is None:
                    layer.append(None)
                else:
                    layer.append(node.val)
                    next_q.append(node.left)
                    next_q.append(node.right)
            if layer != layer[::-1]:
                return False
            layer = []
            queue = next_q
        return True


    def isSymmetric_2(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
        
    def isMirror(self, tree_a, tree_b):
        if tree_a is None and tree_b is None:
            return True
        elif tree_a is None or tree_b is None:
            return False
        else:
            if tree_a.val != tree_b.val:
                return False
            else:
                return self.isMirror(tree_a.left, tree_b.right) and self.isMirror(tree_a.right, tree_b.left)


"""
https://leetcode-cn.com/problems/symmetric-tree/comments/64861
https://leetcode-cn.com/problems/symmetric-tree/comments/158689
"""

"""
class Solution {
public:
    bool check(TreeNode *u, TreeNode *v) {
        queue <TreeNode*> q;
        q.push(u); q.push(v);
        while (!q.empty()) {
            u = q.front(); q.pop();
            v = q.front(); q.pop();
            if (!u && !v) continue;
            if ((!u || !v) || (u->val != v->val)) return false;

            q.push(u->left); 
            q.push(v->right);

            q.push(u->right); 
            q.push(v->left);
        }
        return true;
    }

    bool isSymmetric(TreeNode* root) {
        return check(root, root);
    }
};

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode-solution/
"""