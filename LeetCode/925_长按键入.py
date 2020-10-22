# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 925. 长按键入
Website: https://leetcode-cn.com/problems/long-pressed-name/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了32.20%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了5.44%的用户
=================================================="""


class Solution:
    '''
    你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
    你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
    '''

    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False

        if name[0] != typed[0]:
            return False

        i, j = 1, 1
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif typed[j] == name[i-1]:
                j += 1
            else:
                return False

        return i == len(name) and j == len(typed)

    def isLongPressedName2(self, name: str, typed: str) -> bool:
        # https://leetcode-cn.com/problems/long-pressed-name/solution/chang-an-jian-ru-by-leetcode-solution/634544

        i, j = 0, 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        
        return i == len(name)
