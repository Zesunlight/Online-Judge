/*
=================================================
Problem: 面试题 68 - I. 二叉搜索树的最近公共祖先
Website: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
Difficulty: 简单
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 6 ms, 在所有 Python3 提交中击败了100.00%的用户
Memory Usage: 41.3 MB, 在所有 Python3 提交中击败了18.35%的用户
==================================================*/


class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == q || root == p) return root;
        if (p.val < root.val) {
            if (q.val < root.val) return lowestCommonAncestor(root.left, p, q);
            else return root;
        } else {
            if (q.val < root.val) return root;
            else return lowestCommonAncestor(root.right, p, q);
        }
    }
}


class Solution2 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while(root != null) {
            if(root.val < p.val && root.val < q.val) // p,q 都在 root 的右子树中
                root = root.right; // 遍历至右子节点
            else if(root.val > p.val && root.val > q.val) // p,q 都在 root 的左子树中
                root = root.left; // 遍历至左子节点
            else break;
        }
        return root;
    }
}


class Solution3 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root.val < p.val && root.val < q.val)
            return lowestCommonAncestor(root.right, p, q);
        if(root.val > p.val && root.val > q.val)
            return lowestCommonAncestor(root.left, p, q);
        return root;
    }
}

// 作者：jyd
// 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-i-er-cha-sou-suo-shu-de-zui-jin-g-7/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
