import java.util.*;

/*
    538. 把二叉搜索树转换为累加树
    https://leetcode-cn.com/problems/convert-bst-to-greater-tree/

    给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

    执行用时：4 ms, 在所有 Java 提交中击败了10.37%的用户
    内存消耗：38.9 MB, 在所有 Java 提交中击败了74.75%的用户
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
    public TreeNode convertBST(TreeNode root) {
        if (root == null) return root;
        TreeNode temp = root, res = root;
        LinkedList<TreeNode> stack = new LinkedList<>();
        List<Integer> value = new ArrayList<>();
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.addLast(root);
                root = root.left;
            }
            root = stack.pollLast();
            value.add(root.val);
            root = root.right;
        }

        int sum = 0;
        for (int i = 0; i < value.size(); i++) {
            sum += value.get(i);
        }
        sum -= value.get(0);
        value.add(0);
        int idx = 1;

        while (temp != null || !stack.isEmpty()) {
            while (temp != null) {
                stack.addLast(temp);
                temp = temp.left;
            }
            temp = stack.pollLast();
            temp.val += sum;
            sum -= value.get(idx);
            idx++;
            temp = temp.right;
        }

        return res;
    }
}


class Solution2 {
    int sum = 0;

    public TreeNode convertBST(TreeNode root) {
        if (root != null) {
            convertBST(root.right);
            sum += root.val;
            root.val = sum;
            convertBST(root.left);
        }
        return root;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree/solution/ba-er-cha-sou-suo-shu-zhuan-huan-wei-lei-jia-sh-14/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。