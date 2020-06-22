# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题41. 数据流中的中位数
Website: https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 372 ms, 在所有 Python3 提交中击败了34.91%的用户
Memory Usage: 24.3 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class MedianFinder:
    '''
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.n = []


    def addNum(self, num: int) -> None:
        i = self.find_index(num)
        self.n.insert(i, num)
    
    
    def find_index(self, target):
        left, right = 0, len(self.n) - 1
        while left <= right:
            middle = left + ((right - left) >> 1)
            if target < self.n[middle]:
                right = middle - 1
            elif target > self.n[middle]:
                left = middle + 1
            else:
                return middle
        return left


    def findMedian(self) -> float:
        if len(self.n) % 2 == 0:
            return (self.n[len(self.n) // 2] + self.n[len(self.n) // 2 - 1]) / 2
        else:
            return self.n[len(self.n) // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



from heapq import *

class MedianFinder_2:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
'''
建立一个 小顶堆 A 和 大顶堆 B ，各保存列表的一半元素
随后，中位数可仅根据 A, B 的堆顶元素计算得到

作者：jyd
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian-shi-ti-41-shu-ju-liu-zhong-de-zhong-wei-shu-y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''