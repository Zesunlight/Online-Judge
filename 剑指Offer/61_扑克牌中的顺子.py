# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题61. 扑克牌中的顺子
Website: https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms, 在所有 Python3 提交中击败了43.66%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
    2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
    """
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        king = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                king += 1
            else:
                if i > 0 and nums[i] == nums[i - 1]:
                    return False
        if (nums[-1] - nums[king] + 1 - (len(nums) - king)) <= king:
            return True
        return False

"""
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue # 跳过大小王
            ma = max(ma, num) # 最大牌
            mi = min(mi, num) # 最小牌
            if num in repeat: return False # 若有重复，提前返回 false
            repeat.add(num) # 添加牌至 Set
        return ma - mi < 5 # 最大牌 - 最小牌 < 5 则可构成顺子 

作者：jyd
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
