# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printListNode(self):
        printNode(self)
        print('\n')

def printNode(l):
    if l.next:
        printNode(l.next)
        print(l.val, end = '')
    else:
        print(l.val, end = '')


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        r = ListNode(0)
        while True:

            r.val = (l1.val + l2.val + c) % 10  # sum
            c = (l1.val + l2.val + c) // 10 # carrying

            if l1.next == None:
                if c == 1:
                    r.next = self.numberAddOne(l2.next)
                else:
                    r.next = l2.next
                break
            elif l2.next == None:
                if c == 1:
                    r.next = self.numberAddOne(l1.next)
                else:
                    r.next = l1.next
                break
            else:
                if c == 1:
                    r.next = self.addTwoNumbers(self.numberAddOne(l1.next), l2.next)
                else:
                    r.next = self.addTwoNumbers(l1.next, l2.next)
                break

        return r


    def numberAddOne(self, l):
        if l == None:
            return ListNode(1)

        r = ListNode(0)
        if l.val + 1 == 10:
            if l.next == None:
                r.next = ListNode(1)
            else:
                r.next = self.numberAddOne(l.next)
        else:
            r.val = l.val + 1
            r.next = l.next
        
        return r


a = ListNode(9)
a.next = ListNode(2)
a.printListNode()
b = ListNode(2)
b.next = ListNode(3)
b.printListNode()
c = Solution().addTwoNumbers(a, b)
c.printListNode()


"""
class Solution:
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next
"""