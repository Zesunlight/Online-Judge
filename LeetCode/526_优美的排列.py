# -*- coding: UTF-8 -*-
"""=================================================
Problem: 526. 优美的排列
Website: https://leetcode-cn.com/problems/beautiful-arrangement/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 892 ms
Memory Usage: 15 MB
=================================================="""
from collections import defaultdict
from typing import List
from pprint import pprint

"""
假设有从 1 到 N 的N个整数，如果从这N个数字中成功构造出一个数组，
使得数组的第 i位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。
条件：
第i位的数字能被i整除
i 能被第 i 位上的数字整除
现在给定一个整数 N，请问可以构造多少个优美的排列？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/beautiful-arrangement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countArrangement(self, n: int) -> int:
        factor = {1: [1],
                  2: [1, 2],
                  3: [1, 3],
                  4: [1, 2, 4],
                  5: [1, 5],
                  6: [1, 2, 3, 6],
                  7: [1, 7],
                  8: [1, 2, 4, 8],
                  9: [1, 3, 9],
                  10: [1, 2, 5, 10],
                  11: [1, 11],
                  12: [1, 2, 3, 4, 6, 12],
                  13: [1, 13],
                  14: [1, 2, 7, 14],
                  15: [1, 3, 5, 15]}
        beauty = 0

        not_vitist = set(range(1, 1 + n))

        def backstrace(pos):
            if pos == n + 1:
                nonlocal beauty
                beauty += 1
            temp = list(not_vitist)
            for i in temp:
                if pos in factor[i] or pos % i == 0:
                    not_vitist.remove(i)
                    backstrace(pos + 1)
                    not_vitist.add(i)

        backstrace(1)
        return beauty

    def f(self, n):
        r = []
        for i in range(1, n + 1):
            if n % i == 0:
                r.append(i)
        print(str(n) + ': ' + str(r) + ',')

    def countArrangement2(self, n: int) -> int:
        # https://leetcode-cn.com/problems/beautiful-arrangement/solution/you-mei-de-pai-lie-by-leetcode-solution-vea2/
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)

        num = 0
        vis = set()

        def backtrack(index: int) -> None:
            if index == n + 1:
                nonlocal num
                num += 1
                return

            for x in match[index]:
                if x not in vis:
                    vis.add(x)
                    backtrack(index + 1)
                    vis.discard(x)

        backtrack(1)
        return num


if __name__ == '__main__':
    solution = Solution()
    # for i in range(1, 16):
    #     solution.f(i)
    print(solution.countArrangement(15))
