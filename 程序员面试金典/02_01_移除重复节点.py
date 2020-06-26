# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题02.01. 移除重复节点
Website: https://leetcode-cn.com/problems/remove-duplicate-node-lcci/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 100 ms, 在所有 Python3 提交中击败了40.58%的用户
Memory Usage: 19.9 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
    """
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        root = head
        temp = root
        v = {head.val}
        node = head.next
        while node:
            if node.val not in v:
                temp.next = ListNode(node.val)
                temp = temp.next
                v.add(node.val)
            node = node.next
        return root

    def removeDuplicateNodes_2(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = {head.val}
        pos = head
        # 枚举前驱节点
        while pos.next:
            # 当前待删除节点
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head
    """
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci/solution/yi-chu-zhong-fu-jie-dian-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
