# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 763. 划分字母区间
Website: https://leetcode-cn.com/problems/partition-labels/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了79.44%的用户
Memory Usage: 13.5 MB, 在所有 Python3 提交中击败了9.81%的用户
=================================================="""


class Solution:
    '''
    字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。
    返回一个表示每个字符串片段的长度的列表。
    '''

    def partitionLabels(self, S: str) -> List[int]:
        scope = dict()
        for i in range(len(S)):
            if S[i] in scope:
                scope[S[i]][1] = i
            else:
                scope[S[i]] = [i, i]
        
        result = []
        start, end = 0, scope[S[0]][1]
        for i in range(len(S)):
            if end == i:
                result.append(end - start + 1)
                start = end + 1
                if i < len(S) - 1:
                    end = scope[S[i+1]][1]
            else:
                end = max(end, scope[S[i]][1])
        
        return result


class Solution2:
    def partitionLabels(self, S: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i
        
        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        
        return partition

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/partition-labels/solution/hua-fen-zi-mu-qu-jian-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。