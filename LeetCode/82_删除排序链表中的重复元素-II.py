# -*- coding: UTF-8 -*-
"""=================================================
Problem: 82. 删除排序链表中的重复元素 II
Website: https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 56 ms
Memory Usage: 16.91 MB
=================================================="""
from typing import List, Dict, Set, Optional
from collections import defaultdict, deque, Counter
from itertools import product
from pprint import pprint
import numpy as np
import copy

"""
给定一个已排序的链表的头 head ，删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
"""


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-101)
        res.next = head

        temp = res
        while temp and temp.next and temp.next.next:
            stand = temp
            start = temp.next
            back = temp.next.next
            curr_val = temp.next.val
            while back and back.val == curr_val:
                back = back.next
                start = stand
            start.next = back
            temp = start

        return res.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        # https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/solutions/678122/shan-chu-pai-xu-lian-biao-zhong-de-zhong-oayn/
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    h = ListNode()
    later = h
    for i in [1]:
        later.next = ListNode(i)
        later = later.next
    result = solution.deleteDuplicates(h.next)
    while result:
        print(result.val)
        result = result.next
