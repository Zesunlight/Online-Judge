import java.util.*;

/*
    99. 恢复二叉搜索树
    https://leetcode-cn.com/problems/recover-binary-search-tree/

    二叉搜索树中的两个节点被错误地交换。
    请在不改变其结构的情况下，恢复这棵树。

    执行用时：3 ms, 在所有 Java 提交中击败了53.96%的用户
    内存消耗：40.2 MB, 在所有 Java 提交中击败了38.23%的用户
 */


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


class Solution {
    List<TreeNode> tree = new ArrayList<>();
    TreeNode first, second;
    public void recoverTree(TreeNode root) {
        recoverTree(root, 0);
        int temp = first.val;
        first.val = second.val;
        second.val = temp;
    }

    public void recoverTree(TreeNode root, int fill) {
        if (root == null || fill == 2) return;
        recoverTree(root.left, fill);
        if (tree.size() > 0) {
            TreeNode last = tree.get(tree.size() - 1);
            if (last.val > root.val) {
                second = root;
                if (first == null) {
                    first = last;
                    fill = 1;
                } else {
                    fill = 2;
                }
            }
        }
        tree.add(root);
        recoverTree(root.right, fill);
    }
}


class LeetCode {
    public static void main(String[] args) {
        Solution s = new Solution();
        TreeNode r = new TreeNode(3);
        r.left = new TreeNode(1);
        r.right = new TreeNode(4);
        r.right.left = new TreeNode(2);
        s.recoverTree(r);
        System.out.println(s);
    }
}


class Solution2 {
    public void recoverTree(TreeNode root) {
        Deque<TreeNode> stack = new ArrayDeque<TreeNode>();
        TreeNode x = null, y = null, pred = null;

        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (pred != null && root.val < pred.val) {
                y = root;
                if (x == null) {
                    x = pred;
                } else {
                    break;
                }
            }
            pred = root;
            root = root.right;
        }

        swap(x, y);
    }

    public void swap(TreeNode x, TreeNode y) {
        int tmp = x.val;
        x.val = y.val;
        y.val = tmp;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/recover-binary-search-tree/solution/hui-fu-er-cha-sou-suo-shu-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    // Morris 中序遍历
    
    public void recoverTree(TreeNode root) {
        TreeNode x = null, y = null, pred = null, predecessor = null;

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
                    if (pred != null && root.val < pred.val) {
                        y = root;
                        if (x == null) {
                            x = pred;
                        }
                    }
                    pred = root;

                    predecessor.right = null;
                    root = root.right;
                }
            }
            // 如果没有左孩子，则直接访问右孩子
            else {
                if (pred != null && root.val < pred.val) {
                    y = root;
                    if (x == null) {
                        x = pred;
                    }
                }
                pred = root;
                root = root.right;
            }
        }
        swap(x, y);
    }

    public void swap(TreeNode x, TreeNode y) {
        int tmp = x.val;
        x.val = y.val;
        y.val = tmp;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/recover-binary-search-tree/solution/hui-fu-er-cha-sou-suo-shu-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。