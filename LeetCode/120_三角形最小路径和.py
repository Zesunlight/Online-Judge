# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 120. 三角形最小路径和
Website: https://leetcode-cn.com/problems/triangle/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了48.93%的用户
Memory Usage: 14 MB, 在所有 Python3 提交中击败了9.09%的用户
=================================================="""

class Solution:
    '''
    给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
    相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
    '''
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j - 1 >= 0 and j < len(triangle[i - 1]):
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
                elif j - 1 >= 0:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j]
        return min(triangle[-1])


