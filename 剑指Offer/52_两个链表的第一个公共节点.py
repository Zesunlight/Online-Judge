# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题52. 两个链表的第一个公共节点
Website: https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 180 ms, 在所有 Python3 提交中击败了83.10%的用户
Memory Usage: 29.8 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    输入两个链表，找出它们的第一个公共节点。
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node = {}
        sky, earth = headA, headB
        while sky or earth:
            if sky:
                if sky in node:
                    return sky
                node[sky] = True
                sky = sky.next
            elif earth:
                if earth in node:
                    return earth
                node[earth] = True
                earth = earth.next
        return None


"""
我们使用两个指针 node1，node2 分别指向两个链表 headA，headB 的头结点，然后同时分别逐结点遍历，
当 node1 到达链表 headA 的末尾时，重新定位到链表 headB 的头结点；
当 node2 到达链表 headB 的末尾时，重新定位到链表 headA 的头结点。
这样，当它们相遇时，所指向的结点就是第一个公共结点，走过相同的距离


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1

作者：z1m
链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/shuang-zhi-zhen-fa-lang-man-xiang-yu-by-ml-zimingm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

"""
寻找不变的东西
"""
