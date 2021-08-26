# -*- coding: UTF-8 -*-
"""=================================================
Problem: 223. 矩形面积
Website: https://leetcode-cn.com/problems/rectangle-area/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms
Memory Usage: 15 MB
=================================================="""
from typing import List

"""
给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。
每个矩形由其 左下 顶点和 右上 顶点坐标表示：
第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        yin = self.area(ax1, ay1, ax2, ay2)
        yang = self.area(bx1, by1, bx2, by2)
        cover = yin + yang
        t = self.area(max(ax1, bx1), max(ay1, by1), min(ax2, bx2), min(ay2, by2))
        return cover - t

    def area(self, x1, y1, x2, y2):
        if x2 <= x1 or y2 <= y1:
            return 0
        return (x2 - x1) * (y2 - y1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2))
