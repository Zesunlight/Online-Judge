# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        soldiers = [ListNode] * (n + 1)
        number = 0
        length = 0

        while temp:
            length += 1
            soldiers[number] = temp
            temp = temp.next
            number = (number + 1) % (n + 1)

        if length > n:
            soldiers[number].next = soldiers[(number + 1) % (n + 1)].next
        else:
            head = head.next
        return head

    def printList(self, a):
        while a:
            print(a.val)
            a = a.next

s = [ListNode] * 6
s[0] = ListNode(0)
for i in range(1, 6):
    s[i] = ListNode(i)
    s[i].next = s[i - 1]
a = s[-1]
o = Solution()
o.printList(o.removeNthFromEnd(s[-1], 6))


'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8804/Simple-Java-solution-in-one-pass

public ListNode removeNthFromEnd(ListNode head, int n) {
    
    ListNode start = new ListNode(0);
    ListNode slow = start, fast = start;
    slow.next = head;
    
    //Move fast in front so that the gap between slow and fast becomes n
    for(int i=1; i<=n+1; i++)   {
        fast = fast.next;
    }
    //Move fast to the end, maintaining the gap
    while(fast != null) {
        slow = slow.next;
        fast = fast.next;
    }
    //Skip the desired node
    slow.next = slow.next.next;
    return start.next;
}
'''