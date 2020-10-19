# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 844. 比较含退格的字符串
Website: https://leetcode-cn.com/problems/backspace-string-compare/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms, 在所有 Python3 提交中击败了92.71%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了5.32%的用户
=================================================="""


class Solution:
    """
    给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
    注意：如果对空文本输入退格字符，文本继续为空。
    """
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1, stack2 = [], []
        for i in S:
            if i == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
        for i in T:
            if i == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        return ''.join(stack1) == ''.join(stack2)

    def backspaceCompare2(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        
        return True

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/backspace-string-compare/solution/bi-jiao-han-tui-ge-de-zi-fu-chuan-by-leetcode-solu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。