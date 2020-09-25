import java.util.*;

/*
    501. 二叉搜索树中的众数
    https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/

    给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

    假定 BST 有如下定义：
    结点左子树中所含结点的值小于等于当前结点的值
    结点右子树中所含结点的值大于等于当前结点的值
    左子树和右子树都是二叉搜索树

    执行用时：14 ms, 在所有 Java 提交中击败了6.10%的用户
    内存消耗：40.7 MB, 在所有 Java 提交中击败了12.32%的用户
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
    public int[] findMode(TreeNode root) {
        int times = 0;
        HashMap<Integer, Integer> valTime = new HashMap<>();
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            TreeNode top = stack.pop();
            valTime.put(top.val, valTime.getOrDefault(top.val, 0) + 1);
            int current = valTime.get(top.val);
            if (current > times) {
                result = new ArrayList<>();
                result.add(top.val);
                times = valTime.get(top.val);
            } else if (current == times) {
                result.add(top.val);
            }
            root = top.right;
        }
        
        int[] r = new int[result.size()];
        for (int i = 0; i < r.length; i++) {
            r[i] = result.get(i);
        }
        return r;
    }
}
