import java.util.*;

/*
    111. 二叉树的最小深度
    https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

    给定一个二叉树，找出其最小深度。
    最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

    执行用时：1 ms, 在所有 Java 提交中击败了15.33%的用户
    内存消耗：39.4 MB, 在所有 Java 提交中击败了97.19%的用户
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
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Deque<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 0;

        while (!queue.isEmpty()) {
            int layer = queue.size();
            depth++;
            
            for (int i = 0; i < layer; i++) {
                TreeNode node = queue.poll();
                if (node.left == null && node.right == null) return depth;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        
        return depth;
    }
}
