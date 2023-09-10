# -*- coding: UTF-8 -*-
"""=================================================
Problem: 207. 课程表
Website: https://leetcode.cn/problems/course-schedule/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 872 ms
Memory Usage: 16.92 MB
=================================================="""
from typing import List, Dict, Set
from collections import defaultdict, deque

"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程，先修课程按数组 prerequisites 给出。
其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

(给定有向图，判断其中有无环)
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # https://support.leetcode.cn/hc/kb/article/1194344/
    # 全局变量和类内静态变量需要您手动初始化
    requirement_1: Dict[int, List[int]]

    def canFinish_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time Limit Exceeded
        # 深度优先遍历，找圈
        self.requirement_1 = defaultdict(list)
        for value in prerequisites:
            self.requirement_1[value[0]].append(value[1])
        for course in range(numCourses):
            if self.find_circle(course, {course}):
                return False
        return True

    def find_circle(self, current_course: int, dependency_set: Set[int]) -> bool:
        for depend in self.requirement_1[current_course]:
            if depend in dependency_set:
                return True

            dependency_set.add(depend)
            if self.find_circle(depend, dependency_set):
                return True
            dependency_set.remove(depend)

        return False

    # ------------------------------------------------------------------------------

    requirement_2: Dict[int, Set[int]]

    def canFinish_2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 勉强通过
        # 找入度为0的点，用这些点去更新其他点的依赖
        self.requirement_2 = defaultdict(set)
        for value in prerequisites:
            if value[0] in self.requirement_2:
                self.requirement_2[value[0]].add(value[1])
            else:
                self.requirement_2[value[0]] = {value[1]}

        finish = []
        for course in range(numCourses):
            if len(self.requirement_2[course]) == 0:
                finish.append(course)

        while len(finish) > 0:
            temp = []
            for course in self.requirement_2.keys():
                if len(self.requirement_2[course]) == 0:
                    continue
                for f in finish:
                    self.requirement_2[course].discard(f)
                if len(self.requirement_2[course]) == 0:
                    temp.append(course)
            finish = temp

        for course in self.requirement_2.keys():
            if len(self.requirement_2[course]) > 0:
                return False
        return True

    # ------------------------------------------------------------------------------

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # https://leetcode.cn/problems/course-schedule/solutions/359392/ke-cheng-biao-by-leetcode-solution/
        edges = defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        q = deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(100,
                             [[1, 0], [2, 0], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3], [5, 3], [5, 4], [6, 4], [6, 5],
                              [7, 5], [7, 6], [8, 6], [8, 7], [9, 7], [9, 8], [10, 8], [10, 9], [11, 9], [11, 10],
                              [12, 10], [12, 11], [13, 11], [13, 12], [14, 12], [14, 13], [15, 13], [15, 14], [16, 14],
                              [16, 15], [17, 15], [17, 16], [18, 16], [18, 17], [19, 17], [19, 18], [20, 18], [20, 19],
                              [21, 19], [21, 20], [22, 20], [22, 21], [23, 21], [23, 22], [24, 22], [24, 23], [25, 23],
                              [25, 24], [26, 24], [26, 25], [27, 25], [27, 26], [28, 26], [28, 27], [29, 27], [29, 28],
                              [30, 28], [30, 29], [31, 29], [31, 30], [32, 30], [32, 31], [33, 31], [33, 32], [34, 32],
                              [34, 33], [35, 33], [35, 34], [36, 34], [36, 35], [37, 35], [37, 36], [38, 36], [38, 37],
                              [39, 37], [39, 38], [40, 38], [40, 39], [41, 39], [41, 40], [42, 40], [42, 41], [43, 41],
                              [43, 42], [44, 42], [44, 43], [45, 43], [45, 44], [46, 44], [46, 45], [47, 45], [47, 46],
                              [48, 46], [48, 47], [49, 47], [49, 48], [50, 48], [50, 49], [51, 49], [51, 50], [52, 50],
                              [52, 51], [53, 51], [53, 52], [54, 52], [54, 53], [55, 53], [55, 54], [56, 54], [56, 55],
                              [57, 55], [57, 56], [58, 56], [58, 57], [59, 57], [59, 58], [60, 58], [60, 59], [61, 59],
                              [61, 60], [62, 60], [62, 61], [63, 61], [63, 62], [64, 62], [64, 63], [65, 63], [65, 64],
                              [66, 64], [66, 65], [67, 65], [67, 66], [68, 66], [68, 67], [69, 67], [69, 68], [70, 68],
                              [70, 69], [71, 69], [71, 70], [72, 70], [72, 71], [73, 71], [73, 72], [74, 72], [74, 73],
                              [75, 73], [75, 74], [76, 74], [76, 75], [77, 75], [77, 76], [78, 76], [78, 77], [79, 77],
                              [79, 78], [80, 78], [80, 79], [81, 79], [81, 80], [82, 80], [82, 81], [83, 81], [83, 82],
                              [84, 82], [84, 83], [85, 83], [85, 84], [86, 84], [86, 85], [87, 85], [87, 86], [88, 86],
                              [88, 87], [89, 87], [89, 88], [90, 88], [90, 89], [91, 89], [91, 90], [92, 90], [92, 91],
                              [93, 91], [93, 92], [94, 92], [94, 93], [95, 93], [95, 94], [96, 94], [96, 95], [97, 95],
                              [97, 96], [98, 96], [98, 97], [99, 97]]))
