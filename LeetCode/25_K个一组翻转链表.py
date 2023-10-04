# -*- coding: UTF-8 -*-
"""=================================================
Problem: 25. K 个一组翻转链表
Website: https://leetcode.cn/problems/reverse-nodes-in-k-group
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 68 ms
Memory Usage: 16.61 MB
=================================================="""
from typing import List, Dict, Set, Optional

"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        start = ListNode(0, head)
        first = True
        res = None
        while True:
            group_start = start.next
            group_end = start.next
            for _ in range(k - 1):
                group_end = group_end.next
                if group_end is None:
                    return res
            temp = group_end.next
            group_end.next = None
            s, e = self.reverse(group_start)
            start.next = s
            if first:
                res = s
                first = False
            e.next = temp
            start = e
            if start.next is None:
                return res

    def reverse(self, head: ListNode) -> (ListNode, ListNode):
        """
        翻转链表，返回头尾
        """
        if head is None or head.next is None:
            return head, head

        end = head
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre, end


if __name__ == '__main__':
    solution = Solution()
    first = ListNode(1)
    pre = first
    for i in range(2, 6):
        temp = ListNode(i)
        pre.next = temp
        pre = temp
    result = solution.reverseKGroup(head=first, k=5)

    while result:
        print(result.val)
        result = result.next

