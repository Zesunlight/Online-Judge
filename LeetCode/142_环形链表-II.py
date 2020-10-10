# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 142. 环形链表 II
Website: https://leetcode-cn.com/problems/linked-list-cycle-ii/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 68 ms, 在所有 Python3 提交中击败了47.77%的用户
Memory Usage: 16.9 MB, 在所有 Python3 提交中击败了5.13%的用户
=================================================="""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 
    如果 pos 是 -1，则在该链表中没有环。

    说明：不允许修改给定的链表。
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        pos = 0
        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next
            pos += 1
        return None


"""
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode slow = head, fast = head;
        while (fast != null) {
            slow = slow.next;
            if (fast.next != null) {
                fast = fast.next.next;
            } else {
                return null;
            }
            if (fast == slow) {
                ListNode ptr = head;
                while (ptr != slow) {
                    ptr = ptr.next;
                    slow = slow.next;
                }
                return ptr;
            }
        }
        return null;
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""