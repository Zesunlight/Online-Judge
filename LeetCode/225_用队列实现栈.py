# -*- coding: UTF-8 -*-
"""=================================================
Problem: 225. 用队列实现栈
Website: https://leetcode.cn/problems/implement-stack-using-queues/description/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms
Memory Usage: 16.56 MB
=================================================="""
from collections import deque

'''
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int popleft() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
'''


class MyStack:

    def __init__(self):
        self.a = deque()
        self.b = deque()

    def push(self, x: int) -> None:
        self.a.append(x)
        if len(self.b) > 0:
            self.b.popleft()
        self.b.append(x)

    def pop(self) -> int:
        if len(self.a) == 1:
            self.a.popleft()
            return self.b.popleft()

        head = self.a.popleft()
        self.b.popleft()
        while len(self.a) > 0:
            pre = head
            self.b.append(head)
            head = self.a.popleft()
        self.a, self.b = self.b, self.a
        self.b.append(pre)
        return head

    def top(self) -> int:
        head = self.b.popleft()
        self.b.append(head)
        return head

    def empty(self) -> bool:
        return len(self.a) == 0


class MyStack2:
    # https://leetcode.cn/problems/implement-stack-using-queues/solutions/432204/yong-dui-lie-shi-xian-zhan-by-leetcode-solution/
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1


class MyStack:
    # https://leetcode.cn/problems/implement-stack-using-queues/solutions/432204/yong-dui-lie-shi-xian-zhan-by-leetcode-solution/

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            # 依次出队并入队到队列
            # 队列的前端和后端分别对应栈顶和栈底
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.popleft()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == '__main__':
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(2)
    print(my_stack.top())
    print(my_stack.pop())
