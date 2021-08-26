# -*- coding: UTF-8 -*-
"""=================================================
Problem: 881. 救生艇
Website: https://leetcode-cn.com/problems/boats-to-save-people/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 96 ms
Memory Usage: 20 MB
=================================================="""
from typing import List

"""
第i个人的体重为people[i]，每艘船可以承载的最大重量为limit。
每艘船最多可同时载两人，但条件是这些人的重量之和最多为limit。
返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        left, right = 0, len(people) - 1
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boat += 1
        if left == right:
            boat += 1
        return boat


if __name__ == '__main__':
    solution = Solution()
    print(solution.numRescueBoats(people=[3, 5, 3, 4], limit=5))
