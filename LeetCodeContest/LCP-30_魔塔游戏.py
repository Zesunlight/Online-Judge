import heapq


class Solution:
    # https://leetcode-cn.com/problems/p0NxJO/

    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1

        change = 0
        life = 0
        monster = []
        for n in nums:
            if n < 0:
                heapq.heappush(monster, n)

            life += n

            if life < 0:
                change += 1
                life += -heapq.heappop(monster)

        return change