import java.util.*;

/*
    129. 求根到叶子节点数字之和
    https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

    给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
    例如，从根到叶子节点路径 1->2->3 代表数字 123。
    计算从根到叶子节点生成的所有数字之和。
    说明: 叶子节点是指没有子节点的节点。

    执行用时:0 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗:35.8 MB, 在所所有 Java 提交中击败了98.06%的用户
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
    int sum = 0;
    
    public int sumNumbers(TreeNode root) {
        if (root != null) {
            leaf(root, 0);
        }
        return sum;
    }
    
    public void leaf(TreeNode root, int number) {
        int value = number * 10 + root.val;
        if (root.left == null && root.right == null) {
            sum += value;
        } else {
            if (root.left != null) {
                leaf(root.left, value); 
            }
            if (root.right != null) {
                leaf(root.right, value);
            }
        } 
    }
}


class Solution2 {
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    public int dfs(TreeNode root, int prevSum) {
        if (root == null) {
            return 0;
        }
        int sum = prevSum * 10 + root.val;
        if (root.left == null && root.right == null) {
            return sum;
        } else {
            return dfs(root.left, sum) + dfs(root.right, sum);
        }
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/qiu-gen-dao-xie-zi-jie-dian-shu-zi-zhi-he-by-leetc/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    public int sumNumbers(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int sum = 0;
        Queue<TreeNode> nodeQueue = new LinkedList<TreeNode>();
        Queue<Integer> numQueue = new LinkedList<Integer>();
        nodeQueue.offer(root);
        numQueue.offer(root.val);
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.poll();
            int num = numQueue.poll();
            TreeNode left = node.left, right = node.right;
            if (left == null && right == null) {
                sum += num;
            } else {
                if (left != null) {
                    nodeQueue.offer(left);
                    numQueue.offer(num * 10 + left.val);
                }
                if (right != null) {
                    nodeQueue.offer(right);
                    numQueue.offer(num * 10 + right.val);
                }
            }
        }
        return sum;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/qiu-gen-dao-xie-zi-jie-dian-shu-zi-zhi-he-by-leetc/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。