/*
    109. 有序链表转换二叉搜索树
    https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

    给定一个二叉树，判断它是否是高度平衡的二叉树。
    本题中，一棵高度平衡二叉树定义为：
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

    执行用时：0 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：40.8 MB, 在所有 Java 提交中击败了74.04%的用户
 */


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
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
    public TreeNode sortedListToBST(ListNode head) {
        int listLength = 0;
        ListNode cur = head;
        while (cur != null) {
            cur = cur.next;
            listLength++;
        }
        return sortedListToBST(head, listLength);
    }

    public TreeNode sortedListToBST(ListNode head, int length) {
        if (length == 0) return null;
        if (length == 1) return new TreeNode(head.val);
        
        ListNode left = head;
        int end = length / 2;
        for (int i = 0; i < end; i++) {
            head = head.next;
        }

        TreeNode root = new TreeNode(head.val);
        root.right = sortedListToBST(head.next, length - end - 1);
        head.next = null;
        root.left = sortedListToBST(left, end);

        return root;
    }
}


class Solution2 {
   public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        return helper(head, null);
    }

    private TreeNode helper(ListNode head, ListNode tail) {
        if (head == tail) return null;

        ListNode slow = head;
        ListNode fast = head;
        // 快慢指针找中点
        while (fast != tail && fast.next != tail) {
            slow = slow.next;
            fast = fast.next.next;
        }

        TreeNode root = new TreeNode(slow.val);
        root.left = helper(head, slow);
        root.right = helper(slow.next, tail);
        return root;
    }
}

// 作者：powcai
// 链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/kuai-man-zhi-zhen-zhao-zhong-dian-by-powcai/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    public TreeNode sortedListToBST(ListNode head) {
        return buildTree(head, null);
    }

    public TreeNode buildTree(ListNode left, ListNode right) {
        if (left == right) {
            return null;
        }
        ListNode mid = getMedian(left, right);
        TreeNode root = new TreeNode(mid.val);
        root.left = buildTree(left, mid);
        root.right = buildTree(mid.next, right);
        return root;
    }

    public ListNode getMedian(ListNode left, ListNode right) {
        ListNode fast = left;
        ListNode slow = left;
        while (fast != right && fast.next != right) {
            fast = fast.next;
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


/*
bfs建树 + dfs填节点值

private:
    void dfsBuild(ListNode*& li, TreeNode* root){
        if (root == NULL)
            return;
        dfsBuild(li, root->left);
        root->val = li->val;
        li = li->next;
        dfsBuild(li, root->right);
    }
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (head == NULL)
            return NULL;
        ListNode* node = head;
        TreeNode* root = new TreeNode(0);
        queue<TreeNode*> que;
        que.push(root);
        node = node->next;
        while (node){
            TreeNode* n = que.front();
            que.pop();
            n->left = new TreeNode(0);
            que.push(n->left);
            node = node->next;
            if (node == NULL){
                break;
            }
            n->right = new TreeNode(0);
            que.push(n->right);
            node = node->next;
        }
        dfsBuild(head, root);
        return root;
    }

https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/550589
*/
