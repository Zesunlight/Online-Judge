/*
=================================================
Problem: 面试题 25. 合并两个排序的链表
Website: https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
Difficulty: 简单
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 1 ms, 在所有 Java 提交中击败了99.31%的用户
Memory Usage: 39.7 MB, 在所有 Java 提交中击败了100.00%的用户
==================================================*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    // 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode r = head;
        while (l1 != null && l2 != null) {
            if (l1.val > l2.val) {
                r.next = new ListNode(l2.val);
                l2 = l2.next;
            } else {
                r.next = new ListNode(l1.val);
                l1 = l1.next;
            }
            r = r.next;
        }
        if (l1 == null) {
            r.next = l2;
        }
        if (l2 == null) {
            r.next = l1;
        }
        return head.next;
    }

    public ListNode mergeTwoLists_2(ListNode l1, ListNode l2) {
        ListNode dum = new ListNode(0), cur = dum;
        while(l1 != null && l2 != null) {
            if(l1.val < l2.val) {
                cur.next = l1;
                l1 = l1.next;
            }
            else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }
        cur.next = l1 != null ? l1 : l2;
        return dum.next;
    }

    // 作者：jyd
    // 链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/solution/mian-shi-ti-25-he-bing-liang-ge-pai-xu-de-lian-b-2/
    // 来源：力扣（LeetCode）
    // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
}
