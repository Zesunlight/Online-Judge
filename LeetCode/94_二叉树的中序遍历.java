import java.util.*;

/*
    94. 二叉树的中序遍历
    https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

    给定一个二叉树，返回它的中序 遍历。

    执行用时:1 ms, 在所有 Java 提交中击败了49.79%的用户
    内存消耗:37.7 MB, 在所所有 Java 提交中击败了95.03%的用户
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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inorder = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        Set<TreeNode> visit = new HashSet<>();
        if (root == null) return inorder;

        stack.offerLast(root);
        while (!stack.isEmpty()) {
            TreeNode top = stack.pollLast();
            if (visit.contains(top)) {
                inorder.add(top.val);
            } else {
                if (top.right != null) stack.offerLast(top.right);
                stack.offerLast(top);
                visit.add(top);
                if (top.left != null) stack.offerLast(top.left);
            }
        }
        
        return inorder;
    }
}


class Solution2 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Deque<TreeNode> stk = new LinkedList<TreeNode>();
        while (root != null || !stk.isEmpty()) {
            while (root != null) {
                stk.push(root);
                root = root.left;
            }
            root = stk.pop();
            res.add(root.val);
            root = root.right;
        }
        return res;
    }
}


class Solution3 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        TreeNode predecessor = null;

        while (root != null) {
            if (root.left != null) {
                // predecessor 节点就是当前 root 节点向左走一步，然后一直向右走至无法走为止
                predecessor = root.left;
                while (predecessor.right != null && predecessor.right != root) {
                    predecessor = predecessor.right;
                }
                
                // 让 predecessor 的右指针指向 root，继续遍历左子树
                if (predecessor.right == null) {
                    predecessor.right = root;
                    root = root.left;
                }
                // 说明左子树已经访问完了，我们需要断开链接
                else {
                    res.add(root.val);
                    predecessor.right = null;
                    root = root.right;
                }
            }
            // 如果没有左孩子，则直接访问右孩子
            else {
                res.add(root.val);
                root = root.right;
            }
        }
        return res;
    }
}


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。