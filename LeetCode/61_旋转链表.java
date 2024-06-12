import java.util.*;

/*
    61. 旋转链表
    https://leetcode.cn/problems/rotate-list/description/

    给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

    执行用时：0 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：41.52 MB, 在所有 Java 提交中击败了52.52%的用户
 */
class Solution {

    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) {
            return null;
        }

        int length = 1;
        ListNode temp = head;
        while (temp.next != null) {
            length++;
            temp = temp.next;
        }
        temp.next = head;

        k %= length;
        for (int i = 1; i < length - k; i++) {
            head = head.next;
        }
        temp = head.next;
        head.next = null;
        return temp;
    }
}

public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.rotateRight(Utils.convertArray2ListNode(new int[]{1,2,3,4,5}), 2));
    }
}
