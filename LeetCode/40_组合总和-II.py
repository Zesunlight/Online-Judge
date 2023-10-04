# -*- coding: UTF-8 -*-
"""=================================================
Problem: 40. 组合总和 II
Website: https://leetcode.cn/problems/combination-sum-ii/description/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 64 ms
Memory Usage: 15.5 MB
=================================================="""
from typing import List, Dict, Set

"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        select = sorted(list(counter.keys()))

        def dfs(pos: int, target: int) -> List[List[int]]:
            if target == 0:
                return [[]]
            if pos >= len(select) or select[pos] > target:
                return []
            res = []
            for i in range(counter[select[pos]] + 1):
                part = dfs(pos + 1, target - select[pos] * i)
                for item in part:
                    res.append(item + [select[pos]] * i)
            return res

        return dfs(0, target)

    def combinationSum2_2(self, candidates: List[int], target: int) -> List[List[int]]:
        # https://leetcode.cn/problems/combination-sum-ii/solutions/14753/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
