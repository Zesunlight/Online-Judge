import java.util.*;

/*
    145. 二叉树的后序遍历
    https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

    给定一个二叉树，返回它的 后序 遍历。

    执行用时：1 ms, 在所有 Java 提交中击败了58.06%的用户
    内存消耗：37.3 MB, 在所有 Java 提交中击败了8.09%的用户
 */


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> postorder = new ArrayList<>();
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) return postorder;
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode top = stack.pop();
            postorder.add(top.val);
            if (top.left != null) stack.push(top.left);
            if (top.right != null) stack.push(top.right);
        }
        Collections.reverse(postorder);
        return postorder;
    }
}


class Solution2 {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) {
            return res;
        }

        Deque<TreeNode> stack = new LinkedList<TreeNode>();
        TreeNode prev = null;
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (root.right == null || root.right == prev) {
                res.add(root.val);
                prev = root;
                root = null;
            } else {
                stack.push(root);
                root = root.right;
            }
        }
        return res;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-hou-xu-bian-li-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。