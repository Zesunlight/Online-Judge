import java.util.*;

/*
    106. 从中序与后序遍历序列构造二叉树
    https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

    根据一棵树的中序遍历与后序遍历构造二叉树。假设树中没有重复的元素。

    执行用时：14 ms, 在所有 Java 提交中击败了8.10%的用户
    内存消耗：89 MB, 在所有 Java 提交中击败了5.02%的用户
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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || inorder.length == 0) return null;
        int n = inorder.length;
        TreeNode root = new TreeNode(postorder[n - 1]);
        int left = 0;
        while (inorder[left] != root.val) left++;
        root.left = buildTree(Arrays.copyOfRange(inorder, 0, left), 
                Arrays.copyOfRange(postorder, 0, left));
        root.right = buildTree(Arrays.copyOfRange(inorder, left + 1, n),
                Arrays.copyOfRange(postorder, left, n - 1));
        return root;
    }
}


class Solution2 {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (postorder == null || postorder.length == 0) {
            return null;
        }
        TreeNode root = new TreeNode(postorder[postorder.length - 1]);
        Deque<TreeNode> stack = new LinkedList<TreeNode>();
        stack.push(root);
        int inorderIndex = inorder.length - 1;
        for (int i = postorder.length - 2; i >= 0; i--) {
            int postorderVal = postorder[i];
            TreeNode node = stack.peek();
            if (node.val != inorder[inorderIndex]) {
                node.right = new TreeNode(postorderVal);
                stack.push(node.right);
            } else {
                while (!stack.isEmpty() && stack.peek().val == inorder[inorderIndex]) {
                    node = stack.pop();
                    inorderIndex--;
                }
                node.left = new TreeNode(postorderVal);
                stack.push(node.left);
            }
        }
        return root;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/cong-zhong-xu-yu-hou-xu-bian-li-xu-lie-gou-zao-14/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。