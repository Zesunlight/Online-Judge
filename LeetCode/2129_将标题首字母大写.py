# -*- coding: UTF-8 -*-
"""=================================================
Problem: 2129. 将标题首字母大写
Website: https://leetcode.cn/problems/capitalize-the-title/description/?envType=daily-question&envId=2024-03-11
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 42 ms
Memory Usage: 16.28 MB
=================================================="""

"""
给你一个字符串 title ，它由单个空格连接一个或多个单词组成，每个单词都只包含英文字母。请你按以下规则将每个单词的首字母 大写 ：

如果单词的长度为 1 或者 2 ，所有字母变成小写。
否则，将单词首字母大写，剩余字母变成小写。
请你返回 大写后 的 title 。
"""


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        r = ''
        for word in title.split(' '):
            if len(word) <= 2:
                r += word.lower()
            else:
                r += word.capitalize()
            r += ' '
        return r[:-1]

    def capitalizeTitle2(self, title: str) -> str:
        # https://leetcode.cn/problems/capitalize-the-title/solutions/2679613/jian-ji-xie-fa-pythonjavacgojsrust-by-en-xl5g/
        f = lambda s: s.title() if len(s) > 2 else s.lower()
        return ' '.join(map(f, title.split()))
