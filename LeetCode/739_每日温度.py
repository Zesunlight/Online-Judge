# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 739. 每日温度
Website: https://leetcode-cn.com/problems/daily-temperatures/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 548 ms, 在所有 Python3 提交中击败了65.02%的用户
Memory Usage: 17.7 MB, 在所有 Python3 提交中击败了12.50%的用户
=================================================="""


class Solution:
    """
    根据每日 气温 列表，请重新生成一个列表，
    对应位置的输出是需要再等待多久温度才会升高超过该日的天数。
    如果之后都不会升高，请在该位置用 0 来代替。
    """
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [0]
        res = [0 for _ in range(len(T))]
        for i in range(1, len(T)):
            if not stack or T[i] <= T[stack[-1]]:
                stack.append(i)
            else:
                while stack:
                    top = stack[-1]
                    if T[top] < T[i]:
                        res[top] = i - top
                        stack.pop()
                    else:
                        break
                stack.append(i)
        return res

"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""