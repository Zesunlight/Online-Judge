# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题58 - I. 翻转单词顺序
Website: https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 56 ms, 在所有 Python3 提交中击败了19.81%的用户
Memory Usage: 13.8 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
    为简单起见，标点符号和普通字母一样处理。
    """
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
