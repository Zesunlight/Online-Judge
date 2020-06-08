# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 990. 等式方程的可满足性
Website: https://leetcode-cn.com/problems/satisfiability-of-equality-equations/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了97.21%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了33.33%的用户
=================================================="""


class Solution:
    """
    给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
    并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
    只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 
    """
    def equationsPossible(self, equations) -> bool:
        self.res = {}
        unequal = []
        for equa in equations:
            if equa[1] == "=":
                if (equa[0] not in self.res) and (equa[3] not in self.res):
                    self.res[equa[0]] = equa[0]
                    self.res[equa[3]] = equa[0]
                elif (equa[0] in self.res) and (equa[3] in self.res):
                    self.res[self.find_root(equa[3])] = self.find_root(equa[0])
                elif equa[0] in self.res:
                    self.res[equa[3]] = self.find_root(equa[0])
                else:
                    self.res[equa[0]] = self.find_root(equa[3])
            else:
                unequal.append(equa)
        for n in unequal:
            if (n[0] in self.res) and (n[3] in self.res):
                if self.find_root(n[0]) == self.find_root(n[3]):
                    return False
            elif (n[0] not in self.res) and (n[3] not in self.res) and (n[0] == n[3]):
                return False
        return True

    def find_root(self, var):
        temp = var
        while var != self.res[var]:
            var = self.res[var]
        while temp != self.res[temp]:
            temp = self.res[temp]
            self.res[temp] = var
        return var


s = Solution()
print(s.equationsPossible(["a==b","a!=a"]))

"""

"""
