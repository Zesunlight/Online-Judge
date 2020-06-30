import java.util.*;

/*
    面试题 09. 用两个栈实现队列
    https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

    用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
    分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

    执行用时：55 ms, 在所有 Java 提交中击败了85.59%的用户
    内存消耗：47.5 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class CQueue {
    Deque<Integer> stack;
    Deque<Integer> reverse_s;

    public CQueue() {
        stack = new ArrayDeque<Integer>();
        reverse_s = new ArrayDeque<Integer>();
    }

    public void appendTail(int value) {
        stack.push(value);
    }

    public int deleteHead() {
        if (reverse_s.size() == 0) {
            if (stack.size() == 0) {
                return -1;
            }
            while (stack.size() > 0) {
                reverse_s.push(stack.pop());
            }
        }
        return reverse_s.pop();
    }
}