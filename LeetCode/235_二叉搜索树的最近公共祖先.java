import java.util.*;

/*
    235. 二叉搜索树的最近公共祖先
    https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

    给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

    执行用时：6 ms, 在所有 Java 提交中击败了99.70%的用户
    内存消耗：40.1 MB, 在所有 Java 提交中击败了5.05%的用户
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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (p.val == root.val ||
            q.val == root.val ||
            (p.val < root.val && root.val < q.val) ||
            (p.val > root.val && root.val > q.val)) return root;
        if (p.val < root.val) {
            return lowestCommonAncestor(root.left, p, q);
        } else {
            return lowestCommonAncestor(root.right, p, q);
        }
    }
}


class Solution2 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode ancestor = root;
        while (true) {
            if (p.val < ancestor.val && q.val < ancestor.val) {
                ancestor = ancestor.left;
            } else if (p.val > ancestor.val && q.val > ancestor.val) {
                ancestor = ancestor.right;
            } else {
                break;
            }
        }
        return ancestor;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-26/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。