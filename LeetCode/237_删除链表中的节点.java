/*
    237. 删除链表中的节点
    https://leetcode-cn.com/problems/add-digits/submissions/

    请编写一个函数，用于 删除单链表中某个特定节点 。
    在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问要被删除的节点 。
    题目数据保证需要删除的节点 不是末尾节点 。

    执行用时：0 ms
    内存消耗：37.7 MB
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}


public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution);
    }
}
