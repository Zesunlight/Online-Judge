# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 94. 二叉树的中序遍历
Website: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms, 在所有 Python3 提交中击败了66.87%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了7.84%的用户
=================================================="""


class Solution:
    """
    给定一个二叉树，返回它的中序 遍历。
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            res.extend(self.inorderTraversal(root.right))
        return res

"""
public class Solution {
    public List < Integer > inorderTraversal(TreeNode root) {
        List < Integer > res = new ArrayList < > ();
        Stack < TreeNode > stack = new Stack < > ();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
}

作者：LeetCode
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
