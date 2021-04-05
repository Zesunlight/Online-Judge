from typing import List
from bisect import bisect_right


class Solution:
    # https://leetcode-cn.com/problems/4xy4Wx/

    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if nums[i] > target - nums[i]:
                break
            index = bisect_right(nums, target - nums[i], i)
            res = (res + index - i - 1) % 1000000007
        return res