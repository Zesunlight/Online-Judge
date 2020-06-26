import java.util.*;

/*
    面试题 02.01. 移除重复节点
    https://leetcode-cn.com/problems/remove-duplicate-node-lcci/

    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

    执行用时：381 ms, 在所有 Java 提交中击败了17.51%的用户
    内存消耗：40.6 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}


class Solution {
    public ListNode removeDuplicateNodes(ListNode head) {
        ListNode wait = head;
        while (wait != null) {
            ListNode run = wait;
            while (run.next != null) {
                if (run.next.val == wait.val) {
                    run.next = run.next.next;
                } else {
                    run = run.next;
                }
            }
            wait = wait.next;
        }
        return head;
    }
}


class LeetCode {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println();
    }
}