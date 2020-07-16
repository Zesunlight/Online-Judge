# -*- coding: UTF-8 -*-
"""=================================================
Problem:    牛牛晾衣服
Website: https://ac.nowcoder.com/acm/contest/6220/C
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""

#
# 计算最少要多少时间可以把所有的衣服全烘干
# @param n int整型 n件衣服
# @param a int整型一维数组 n件衣服所含水量数组
# @param k int整型 烘干机1分钟可以烘干的水量
# @return int整型
#
class Solution:
    def solve(self , n , a , k ):
        # write code here
        import heapq
        h = [-i for i in a]
        heapq.heapify(h)
        nature = 0
        c = heapq.heappop(h)
        while nature > c:
            heapq.heappush(h, c + k - 1)
            c = heapq.heappop(h)
            nature -= 1
        return -nature