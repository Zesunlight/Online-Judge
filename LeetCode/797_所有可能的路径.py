# -*- coding: UTF-8 -*-
"""=================================================
Problem: 797. 所有可能的路径
Website: https://leetcode-cn.com/problems/all-paths-from-source-to-target/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms
Memory Usage: 16.2 MB
=================================================="""
from typing import List

"""
给你一个有n个节点的 有向无环图（DAG），请你找出所有从节点 0到节点 n-1的路径并输出（不要求按特定顺序）
二维数组的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些节点，空就是没有下一个结点了。
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        n = len(graph)

        def dfs(point, trace: List[int]):
            for follow in graph[point]:
                trace.append(follow)
                if follow == n - 1:
                    path.append(trace.copy())
                else:
                    dfs(follow, trace)
                trace.pop()

        dfs(0, [0])
        return path


if __name__ == '__main__':
    solution = Solution()
    print(solution.allPathsSourceTarget([[1], []]))
