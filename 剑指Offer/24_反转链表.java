/*
=================================================
Problem: 面试题 24. 反转链表
Website: https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
Difficulty: 简单
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 0 ms, 在所有 Java 提交中击败了100.00%的用户
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
    // 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

    public ListNode reverseList(ListNode head) {
        if (head == null) return null;
        ListNode cur = new ListNode(head.val);
        head = head.next;
        while (head != null) {
            ListNode temp = new ListNode(head.val);
            temp.next = cur;
            cur = temp;
            head = head.next;
        }
        return cur;
    }
}

/*
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = NULL, *pre = head;
        while (pre != NULL) {
            ListNode* t = pre->next;
            pre->next = cur;
            cur = pre;
            pre = t;
        }
        return cur;
    }
};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        ListNode* ret = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return ret;
    }
};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL) { return NULL; }
        ListNode* cur = head;
        while (head->next != NULL) {
            ListNode* t = head->next->next;
            head->next->next = cur;
            cur = head->next;
            head->next = t;
        }
        return cur;
    }
};

作者：huwt
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/fan-zhuan-lian-biao-yi-dong-de-shuang-zhi-zhen-jia/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

*/