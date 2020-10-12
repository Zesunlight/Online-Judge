import java.util.*;

/*
    530. 二叉搜索树的最小绝对差
    https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/

    给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

    执行用时：1 ms, 在所有 Java 提交中击败了82.39%的用户
    内存消耗：38.4 MB, 在所有 Java 提交中击败了87.06%的用户
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
    int pre;
    int ans;

    public int getMinimumDifference(TreeNode root) {
        ans = Integer.MAX_VALUE;
        pre = -1;
        dfs(root);
        return ans;
    }

    public void dfs(TreeNode root) {
        if (root == null) {
            return;
        }
        dfs(root.left);
        if (pre == -1) {
            pre = root.val;
        } else {
            ans = Math.min(ans, root.val - pre);
            pre = root.val;
        }
        dfs(root.right);
    }
}


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/solution/er-cha-sou-suo-shu-de-zui-xiao-jue-dui-chai-by-lee/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。