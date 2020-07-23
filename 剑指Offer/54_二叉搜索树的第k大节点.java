/*
=================================================
Problem: 面试题 54. 二叉搜索树的第k大节点
Website: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/submissions/
Difficulty: 简单
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 0 ms, 在所有 Python3 提交中击败了100.00%的用户
Memory Usage: 38.9 MB, 在所有 Python3 提交中击败了100.00%的用户
==================================================*/


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
    int[] res;
    int index = 0;
    public int kthLargest(TreeNode root, int k) {
        res = new int[k];
        fill(root);
        return res[k - 1];
    }

    public boolean fill(TreeNode root) {
        if (root == null) {
            return false;
        }
        if (fill(root.right)) return true;
        res[index++] = root.val;
        if (index == res.length) {
            return true;
        }
        if (fill(root.left)) return true;
        return false;
    }
}
