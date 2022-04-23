from math import ceil


class Solution:
    # https://leetcode-cn.com/problems/PTXy4P/

    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        res = 0
        for type, num in fruits:
            res += (ceil(num / limit)) * time[type]
        return res
