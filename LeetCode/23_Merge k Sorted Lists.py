# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:

        value = []
        for i in lists:
            t = i
            while t:
                value.append(t.val)
                t = t.next

        if len(value) == 0:
            return []

        value.sort(reverse=True)
        node = [ListNode] * len(value)
        node[0] = ListNode(value[0])

        for i in range(1, len(value)):
            node[i] = ListNode(value[i])
            node[i].next = node[i - 1]

        return node[-1]

    def printList(self, a):
        while a:
            print(a.val)
            a = a.next
        print("-----------------")

s = [ListNode] * 3
s[0] = ListNode(3)
for i in range(1, 3):
    s[i] = ListNode(3 - i)
    s[i].next = s[i - 1]
a = s[-1]
b = s[-2]
c = s[-3]
o = Solution()
o.printList(o.mergeKLists([a, b, c]))

'''
Approach 1: Brute Force
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
        
https://leetcode.com/problems/merge-k-sorted-lists/discuss/10531/Sharing-my-straightforward-C++-solution-without-data-structure-other-than-vector        
ListNode *mergeKLists(vector<ListNode *> &lists) {
    if(lists.empty()){
        return nullptr;
    }
    while(lists.size() > 1){
        lists.push_back(mergeTwoLists(lists[0], lists[1]));
        lists.erase(lists.begin());
        lists.erase(lists.begin());
    }
    return lists.front();
}
ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
    if(l1 == nullptr){
        return l2;
    }
    if(l2 == nullptr){
        return l1;
    }
    if(l1->val <= l2->val){
        l1->next = mergeTwoLists(l1->next, l2);
        return l1;
    }
    else{
        l2->next = mergeTwoLists(l1, l2->next);
        return l2;
    }
}
'''