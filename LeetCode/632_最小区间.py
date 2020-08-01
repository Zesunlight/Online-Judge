# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 632. 最小区间
Website: https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
=================================================="""


class Solution:
    """
    你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
    """

    def smallestRange(self, nums):
        # slide window
        # https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/solution/pai-xu-hua-chuang-by-netcan/
        # Runtime: 620 ms, 在所有 Python3 提交中击败了28.10%的用户
        # Memory Usage: 21.3 MB, 在所有 Python3 提交中击败了50.00%的用户

        order = []
        for index, item in enumerate(nums):
            order.extend([(value, index) for value in item])
        order.sort(key=lambda x: x[0])

        include = [0] * len(nums)
        start, end = 0, 0
        ans = [order[0][0], order[-1][0]]
        while end < len(order):
            include[order[end][1]] += 1

            if 0 not in include:
                while include[order[start][1]] > 1:
                    include[order[start][1]] -= 1
                    start += 1

                if order[end][0] - order[start][0] < ans[1] - ans[0]:
                    ans[0], ans[1] = order[start][0], order[end][0]

                include[order[start][1]] -= 1
                start += 1

            end += 1

        return ans


    def smallestRange_2(self, nums):
        # k pointers
        # https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/solution/zui-xiao-qu-jian-by-coldme-2/
        # Runtime: 284 ms, 在所有 Python3 提交中击败了84.30%的用户
        # Memory Usage: 19.7 MB, 在所有 Python3 提交中击败了50.00%的用户

        candidate = [(item[0], index, 0) for index, item in enumerate(nums)]
        heapq.heapify(candidate)
        ans = [min(candidate)[0], max(candidate)[0]]
        sup = ans[1]
        while 1:
            value, index, pointer = heapq.heappop(candidate)
            if sup - value < ans[1] - ans[0]:
                ans[0], ans[1] = value, sup
            if pointer + 1 >= len(nums[index]):
                break
            sup = max(sup, nums[index][pointer + 1])
            heapq.heappush(candidate, (nums[index][pointer + 1], index, pointer + 1))

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))
