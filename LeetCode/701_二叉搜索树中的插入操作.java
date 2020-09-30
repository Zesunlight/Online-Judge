import java.util.*;

/*
    701. 二叉搜索树中的插入操作
    https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/

    给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 
    返回插入后二叉搜索树的根节点。 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
    注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

    执行用时：14 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：39.6 MB, 在所有 Java 提交中击败了31.99%的用户
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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        List<Integer> value = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        boolean insert = false;
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            TreeNode top = stack.pop();
            value.add(top.val);
            if (!insert && val < top.val) {
                value.add(value.size() - 1, val);
                insert = true;
            }
            root = top.right;
        }
        if (!insert) value.add(val);
        return buildBST(value);
    }
    
    public TreeNode buildBST(List<Integer> value) {
        if (value.size() == 0) return null;
        if (value.size() == 1) return new TreeNode(value.get(0));
        int rootIndex = value.size() / 2;
        TreeNode root = new TreeNode(value.get(rootIndex));
        root.left = buildBST(value.subList(0, rootIndex));
        root.right = buildBST(value.subList(rootIndex + 1, value.size()));
        return root;
    }
}


class Solution2 {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        TreeNode pos = root;
        while (pos != null) {
            if (val < pos.val) {
                if (pos.left == null) {
                    pos.left = new TreeNode(val);
                    break;
                } else {
                    pos = pos.left;
                }
            } else {
                if (pos.right == null) {
                    pos.right = new TreeNode(val);
                    break;
                } else {
                    pos = pos.right;
                }
            }
        }
        return root;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/solution/er-cha-sou-suo-shu-zhong-de-cha-ru-cao-zuo-by-le-3/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }

        if (root.val < val) {
            root.right = insertIntoBST(root.right, val);
        } else {
            root.left = insertIntoBST(root.left, val);
        }
        return root;
    }
}

// 作者：sweetiee
// 链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/solution/2-de-cha-ru-by-sweetiee/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。