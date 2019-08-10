"""
    Problem: 21. Merge Two Sorted Lists
    Website: https://leetcode.com/problems/merge-two-sorted-lists/
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 44 ms, faster than 63.33% of Python3 online submissions for Merge Two Sorted Lists.
    Memory Usage: 14 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes of the first two lists.
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode(0)
        temp = r
        while l1 or l2:
            temp.next = ListNode(0)
            temp = temp.next

            if l1 is None:
                while l2:
                    temp.val = l2.val
                    l2 = l2.next
                    if l2:
                        temp.next = ListNode(0)
                        temp = temp.next
            elif l2 is None:
                while l1:
                    temp.val = l1.val
                    l1 = l1.next
                    if l1:
                        temp.next = ListNode(0)
                        temp = temp.next
            else:
                if l1.val < l2.val:
                    temp.val = l1.val
                    l1 = l1.next
                else:
                    temp.val = l2.val
                    l2 = l2.next

        return r.next

    def printList(self, l):
        while l:
            print(l.val)
            l = l.next


s = Solution()
a = ListNode(5)
a.next = ListNode(8)
b = ListNode(3)
b.next = ListNode(9)
res = s.mergeTwoLists(a, b)
print(s.printList(res))


"""
https://leetcode.com/problems/merge-two-sorted-lists/discuss/9715/Java-1-ms-4-lines-codes-using-recursion
public ListNode mergeTwoLists(ListNode l1, ListNode l2){
    if(l1 == null) return l2;
    if(l2 == null) return l1;
    if(l1.val < l2.val){
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    } else{
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
}
"""

"""
https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
    
    
https://leetcode.com/problems/merge-two-sorted-lists/discuss/9714/14-line-clean-C++-Solution
class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode dummy(INT_MIN);
        ListNode *tail = &dummy;
        
        while (l1 && l2) {
            if (l1->val < l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }

        tail->next = l1 ? l1 : l2;
        return dummy.next;
    }
};
"""