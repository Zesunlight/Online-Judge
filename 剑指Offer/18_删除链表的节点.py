# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题18. 删除链表的节点
Website: https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了41.52%的用户
Memory Usage: 13.9 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
    返回删除后的链表的头节点。
    """
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre = head
        cur = head.next
        while 1:
            if cur.val == val:
                pre.next = cur.next
                return head
            pre = cur
            cur = cur.next

"""
https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/solution/mian-shi-ti-18-shan-chu-lian-biao-de-jie-dian-sh-2/342447

class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        if (head == null) return null;
        if (head.val == val) return head.next;
        ListNode cur = head;
        while (cur.next != null && cur.next.val != val)
            cur = cur.next;
        if (cur.next != null)
            cur.next = cur.next.next;
        return head;
    }
}
"""
