/*
    543. 二叉树的直径
    https://leetcode.cn/problems/diameter-of-binary-tree/description/

    给你一棵二叉树的根节点，返回该树的 直径 。
    二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
    两节点之间路径的 长度 由它们之间边数表示。

    执行用时：385 ms
    内存消耗：45.27 MB
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        return findWidth(root);
    }

    public int findWidth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftWidth = findWidth(root.left);
        int rightWidth = findWidth(root.right);
        int bothWidth = findDepth(root.left) + findDepth(root.right);
        return Math.max(Math.max(leftWidth, rightWidth), bothWidth);
    }

    private int findDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(findDepth(root.left), findDepth(root.right));
    }


    // https://leetcode.cn/problems/diameter-of-binary-tree/solutions/139683/er-cha-shu-de-zhi-jing-by-leetcode-solution/
    int ans;
    public int diameterOfBinaryTree2(TreeNode root) {
        ans = 1;  // 节点数量（边的数量 + 1）
        depth(root);
        return ans - 1;
    }
    public int depth(TreeNode node) {
        if (node == null) {
            return 0; // 访问到空节点了，返回0
        }
        int L = depth(node.left); // 左儿子为根的子树的深度
        int R = depth(node.right); // 右儿子为根的子树的深度
        ans = Math.max(ans, L+R+1); // 计算d_node即L+R+1 并更新ans
        return Math.max(L, R) + 1; // 返回该节点为根的子树的深度
    }
}