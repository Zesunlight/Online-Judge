# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 290. 单词规律
Website: https://leetcode-cn.com/problems/word-pattern/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms
Memory Usage: 14.6 MB
=================================================="""


class Solution:
    """
    给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
    这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        unique = set()
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if words[i] in dic:
                if dic[words[i]] != pattern[i]:
                    return False
            else:
                if pattern[i] in unique:
                    return False
                unique.add(pattern[i])
                dic[words[i]] = pattern[i]

        return True
