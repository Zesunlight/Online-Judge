import java.util.*;

/*
    783. 二叉搜索树节点最小距离
    https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/

    给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

    执行用时：1 ms, 在所有 Java 提交中击败了32.27%的用户
    内存消耗：36 MB, 在所有 Java 提交中击败了99.12%的用户
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
    int m = Integer.MAX_VALUE;
    public int minDiffInBST(TreeNode root) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode min = root, back = null;
        while (min != null) {
            back = min;
            min = min.left;
        }
        int pre = Integer.MIN_VALUE + back.val + 1;
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            TreeNode top = stack.pop();
            m = Math.min(m, top.val - pre);
            if (m == 1) break;
            pre = top.val;
            root = top.right;
        }
        return m;
    }
}