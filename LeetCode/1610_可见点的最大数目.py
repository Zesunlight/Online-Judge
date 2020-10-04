# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1610. 可见点的最大数目
Website: https://leetcode-cn.com/problems/maximum-number-of-visible-points/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 588 ms
Memory Usage: 41.6 MB
=================================================="""


class Solution:
    """
    给你一个点数组 points 和一个表示角度的整数 angle ，你的位置是 location ，
    其中 location = [posx, posy] 且 points[i] = [xi, yi] 都表示 X-Y 平面上的整数坐标。

    最开始，你面向东方进行观测。你 不能 进行移动改变位置，但可以通过 自转 调整观测角度。
    换句话说，posx 和 posy 不能改变。你的视野范围的角度用 angle 表示， 这决定了你观测任意方向时可以多宽。
    设 d 为逆时针旋转的度数，那么你的视野就是角度范围 [d - angle/2, d + angle/2] 所指示的那片区域。
    """
    def isEvenOddTree(self, root: TreeNode) -> bool:
        odd = False
        q = deque()
        q.append(root)
        while q:
            l = len(q)
            if odd:
                pre = 10 ** 6 + 1
            else:
                pre = 0
            for _ in range(l):
                top = q.popleft()
                if odd:
                    if top.val % 2 == 0 and top.val < pre:
                        pre = top.val
                    else:
                        return False
                else:
                    if top.val % 2 == 1 and top.val > pre:
                        pre = top.val
                    else:
                        return False
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            odd = not odd
        return True
