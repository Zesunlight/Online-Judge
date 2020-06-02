# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题09. 用两个栈实现队列
Website: https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 2408 ms, 在所有 Python3 提交中击败了10.34%的用户
Memory Usage: 16.9 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class CQueue:
    """
    用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
    """
    def __init__(self):
        self.s1 = []
        self.s2 = []


    def appendTail(self, value: int) -> None:
        self.s1.append(value)


    def deleteHead(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        if self.s2:
            res = self.s2.pop()
            while self.s2:
                self.s1.append(self.s2.pop())
            return res
        else:
            return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


"""
class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()

作者：jyd
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/mian-shi-ti-09-yong-liang-ge-zhan-shi-xian-dui-l-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
