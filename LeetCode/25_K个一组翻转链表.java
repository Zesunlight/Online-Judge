/*
    25. K 个一组翻转链表
    https://leetcode.cn/problems/reverse-nodes-in-k-group/description/

    给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 */

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(-1, head);
        ListNode pre = dummy;
        ListNode start = head;
        ListNode end = head;

        while (end != null) {
            for (int i = 0; i < k - 1; i++) {
                end = end.next;
                if (end == null) {
                    break;
                }
            }

            if (end != null) {
                reverse(start, end);
                pre.next = end;
                pre = start;
                start = start.next;
                end = start;
            }
        }

        return dummy.next;
    }

    private void reverse(ListNode start, ListNode end) {
        ListNode pre = end.next;
        ListNode temp = start;
        while (temp != end) {
            ListNode next = temp.next;
            temp.next = pre;
            pre = temp;
            temp = next;
        }
        end.next = pre;
    }
}

public class Hello {
    public static void main(String[] args) {
        Solution solution = new Solution();
        ListNode dummy = new ListNode(0);
        ListNode temp = dummy;
        for (int i = 1; i <= 10; i++) {
            temp.next = new ListNode(i);
            temp = temp.next;
        }
        ListNode head = solution.reverseKGroup(dummy.next, 3);
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }
}
