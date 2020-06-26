import java.util.*;

/*
    33. 二叉搜索树的后序遍历序列
    https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/

    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
    如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

    执行用时：0 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：37.3 MB, 在所有 Java 提交中击败了100.00%的用户
 */

class Solution {
    public boolean verifyPostorder(int[] postorder) {
        return stick(postorder, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    boolean stick(int[] tree, int inf, int sup) {
        if (inf >= sup) {
            return false;
        }
        if (tree.length == 0) {
            return true;
        }
        if (tree.length == 1) {
            return inf < tree[0] && tree[0] <= sup;
        }

        int root = tree[tree.length - 1];
        int change = 0;
        while (tree[change] < root) {
            ++change;
        }
        int[] left = Arrays.copyOfRange(tree, 0, change);
        int[] right = Arrays.copyOfRange(tree, change, tree.length - 1);

        return stick(left, inf, root) && stick(right, root, sup);
    }
}


class LeetCode {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.verifyPostorder(new int[] {3, 0, 2}));
    }
}