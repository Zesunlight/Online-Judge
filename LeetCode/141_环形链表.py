# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 141. 环形链表
Website: https://leetcode-cn.com/problems/linked-list-cycle/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 68 ms, 在所有 Python3 提交中击败了41.56%的用户
Memory Usage: 16.5 MB, 在所有 Python3 提交中击败了9.52%的用户
=================================================="""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    给定一个链表，判断链表中是否有环。
    """
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        if head == None or head.next == None:
            return False
        fast = head.next.next
        while slow is not fast:
            if fast == None:
                return False
            else:
                if fast.next == None:
                    return False
                fast = fast.next.next
                slow = slow.next
        else:
            return True


"""
链表双指针
"""