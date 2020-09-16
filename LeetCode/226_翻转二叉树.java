import java.util.*;

/*
    226. 翻转二叉树
    https://leetcode-cn.com/problems/invert-binary-tree/

    翻转一棵二叉树。

    执行用时：0 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：36.7 MB, 在所有 Java 提交中击败了5.14%的用户
 */


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root != null) {
            TreeNode temp = root.left;
            root.left = invertTree(root.right);
            root.right = invertTree(temp);
        }
        return root;
    }
}