import java.util.*;

/*
    110. 平衡二叉树
    https://leetcode-cn.com/problems/balanced-binary-tree/

    给定一个二叉树，判断它是否是高度平衡的二叉树。
    本题中，一棵高度平衡二叉树定义为：
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

    执行用时：1 ms, 在所有 Java 提交中击败了99.76%的用户
    内存消耗：39.8 MB, 在所有 Java 提交中击败了69.11%的用户
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
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        if (depth(root) == -1) return false;
        return true;
    }

    public int depth(TreeNode root) {
        if (root == null) return 0;
        int left = depth(root.left), right = depth(root.right);
        if (left == -1 || right == -1 || Math.abs(left - right) >= 2) return -1;
        return Math.max(left, right) + 1;
    }
}
