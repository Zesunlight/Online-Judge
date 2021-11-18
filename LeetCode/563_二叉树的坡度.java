/*
    563. 二叉树的坡度
    https://leetcode-cn.com/problems/binary-tree-tilt/submissions/

    给定一个二叉树，计算 整个树 的坡度 。
    一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。
    如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。
    整个树 的坡度就是其所有节点的坡度之和。

    执行用时：0 ms
    内存消耗：38.6 MB
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    int sum = 0;

    public int findTilt(TreeNode root) {
        tilt(root);
        return sum;
    }

    public int tilt(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = tilt(root.left);
        int right = tilt(root.right);
        sum += Math.abs(left - right);
        return left + right + root.val;
    }
}


public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution);
    }
}
