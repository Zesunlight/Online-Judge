# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 83. 删除排序链表中的重复元素
Website: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms
Memory Usage: 14.9 MB
=================================================="""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        pre = head
        temp = head.next
        while temp is not None:
            if temp.val == pre.val:
                pre.next = temp.next
            else:
                pre = temp
            temp = temp.next
        return head

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head

    # 作者：LeetCode-Solution
    # 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/solution/shan-chu-pai-xu-lian-biao-zhong-de-zhong-49v5/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。