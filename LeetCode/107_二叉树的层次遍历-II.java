import java.util.*;

/*
    107. 二叉树的层次遍历 II
    https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/

    给定一个二叉树，返回其节点值自底向上的层次遍历。 
    （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

    执行用时：1 ms, 在所有 Java 提交中击败了98.25%的用户
    内存消耗：40 MB, 在所有 Java 提交中击败了42.63%的用户
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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        if (root == null) return res;

        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> layer = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
                layer.add(node.val);
            }
            res.add(layer);
        }

        Collections.reverse(res);
        return res;
    }
}
