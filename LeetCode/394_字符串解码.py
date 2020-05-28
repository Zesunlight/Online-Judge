# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 394. 字符串解码
Website: https://leetcode-cn.com/problems/decode-string/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms, 在所有 Python3 提交中击败了62.26%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了20.00%的用户
=================================================="""


class Solution:
    """
    给定一个经过编码的字符串，返回它解码后的字符串。
    编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
    """
    def decodeString(self, s: str) -> str:
        if len(s) <= 1:
            return s

        if s[0].isdigit():
            brace = 0
            end = 1
            enter = False
            for i in range(1, len(s)):
                if s[i] == '[':
                    brace += 1
                    enter = True
                elif s[i] == ']':
                    brace -= 1
                elif s[i].isdigit() and not enter:
                    end += 1
                    continue
                if brace == 0:
                    return int(s[:end]) * self.decodeString(s[end+1:i]) + self.decodeString(s[i+1:])
        else:
            return s[0] + self.decodeString(s[1:])


s = Solution()
print(s.decodeString("3[a2[c]]"))

"""
https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/

栈
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res

递归
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)
"""
