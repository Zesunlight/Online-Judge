# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 145. 二叉树的后序遍历
Website: https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms, 在所有 Python3 提交中击败了65.91%的用户
Memory Usage: 13.8 MB, 在所有 Python3 提交中击败了7.41%的用户
=================================================="""


class Solution:
    """
    给定一个二叉树，返回它的 后序 遍历。
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            res.extend(self.postorderTraversal(root.left))
            res.extend(self.postorderTraversal(root.right))
            res.append(root.val)
        return res

"""
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]

作者：LeetCode
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-hou-xu-bian-li-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

"""
只用栈做后序遍历，难点在于仅利用栈去判断该节点是否为父结点，
创新性思路是每次在栈中压入父节点后压入nullptr，之后再依次压入右子节点和左子节点。

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == nullptr) return {};
        stack<TreeNode*> stk;
        stk.push(root);
        vector<int> res;
        while (!stk.empty()) {
            TreeNode* node = stk.top();
            if (node == nullptr) {
                stk.pop();
                res.push_back(stk.top()->val);
                stk.pop();
                continue;
            }
            stk.push(nullptr);
            if (node->right) {
                stk.push(node->right);
            }
            if (node->left) {
                stk.push(node->left);
            }
        }
        return res;
    }
};

作者：dcoliversun
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/a-li-mian-shi-ti-zhi-yong-zhan-qu-zuo-er-cha-shu-d/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""