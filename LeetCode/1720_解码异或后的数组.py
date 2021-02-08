# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1720. 解码异或后的数组
Website: https://leetcode-cn.com/problems/decode-xored-array/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms
Memory Usage: 16.1 MB
=================================================="""


class Solution:
    """
    未知 整数数组 arr 由 n 个非负整数组成。
    经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。
    例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。
    给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。
    请解码返回原数组 arr 。可以证明答案存在并且是唯一的。
    """
    def decode(self, encoded: List[int], first: int) -> List[int]:
        origin = [first]
        pre = first
        for i in encoded:
            origin.append(i ^ pre)
            pre = origin[-1]
        return origin
