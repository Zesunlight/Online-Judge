# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 785. 判断二分图
Website: https://leetcode-cn.com/problems/is-graph-bipartite/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 224 ms, 在所有 Python3 提交中击败了49.16%的用户
Memory Usage: 13.9 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    '''
    给定一个无向图graph，当这个图为二分图时返回true。

    如果我们能将一个图的节点集合分割成两个独立的子集A和B，
    并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。

    graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。
    每个节点都是一个在0到graph.length-1之间的整数。
    这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。
    '''

    def __init__(self):
        self.A = set()
        self.B = set()
        self.graph = []

    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph = graph
        for i in range(len(graph)):
            if (i not in self.A) and (i not in self.B):
                self.A.add(i)
                if not self.fromA(self.graph[i]):
                    return False
        return True

    def fromA(self, neighborhoods):
        for n in neighborhoods:
            if n in self.A:
                return False

            if n not in self.B:
                self.B.add(n)
                if not self.fromB(self.graph[n]):
                    return False

        return True

    def fromB(self, neighborhoods):
        for n in neighborhoods:
            if n in self.B:
                return False

            if n not in self.A:
                self.A.add(n)
                if not self.fromA(self.graph[n]):
                    return False

        return True

class Solution_2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        valid = True

        def dfs(node: int, c: int):
            nonlocal valid
            color[node] = c
            cNei = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                elif color[neighbor] != cNei:
                    valid = False
                    return

        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    break
        
        return valid

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/is-graph-bipartite/solution/pan-duan-er-fen-tu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution_3:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        
        for i in range(n):
            if color[i] == UNCOLORED:
                q = collections.deque([i])
                color[i] = RED
                while q:
                    node = q.popleft()
                    cNei = (GREEN if color[node] == RED else RED)
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:
                            q.append(neighbor)
                            color[neighbor] = cNei
                        elif color[neighbor] != cNei:
                            return False

        return True

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/is-graph-bipartite/solution/pan-duan-er-fen-tu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
