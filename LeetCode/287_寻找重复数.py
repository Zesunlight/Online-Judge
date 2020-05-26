# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 287. 寻找重复数
Website: https://leetcode-cn.com/problems/find-the-duplicate-number/submissions/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 84 ms, 在所有 Python3 提交中击败了78.97%的用户
Memory Usage: 16.1 MB, 在所有 Python3 提交中击败了35.71%的用户
=================================================="""


class Solution:
    def findDuplicate(self, nums) -> int:
        if len(nums) <= 2:
            return nums[0]

        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


s = Solution()
print(s.findDuplicate([1,2,3,4,5,2]))

"""
https://leetcode-cn.com/problems/find-the-duplicate-number/solution/xun-zhao-zhong-fu-shu-by-leetcode-solution/

https://leetcode-cn.com/problems/find-the-duplicate-number/comments/72234
二分法
    def findDuplicate(self, nums: List[int]) -> int:
        #数组只能读 所以不能排序,不能swap数组下标
        #时间复杂度小于 O(n^2) 不能暴力
        #空间复杂度 O(1) 不能额外开辟数组
        
        '''小于O(n^2) 二分查找
        我们不要考虑数组,只需要考虑 数字都在 1 到 n 之间
        示例 1:
        arr = [1,3,4,2,2] 此时数字在 1 — 5 之间

        mid = (1 + 5) / 2 = 3 arr小于等于的3有4个(1,2,2,3)，1到3中肯定有重复的值
        mid = (1 + 3) / 2 = 2 arr小于等于的2有3个(1,2,2)，1到2中肯定有重复的值
        mid = (1 + 2) / 2 = 1 arr小于等于的1有1个(1)，2到2中肯定有重复的值
        所以重复的数是 2 
        '''
        left = 1
        right = len(nums)
        while left < right:
            mid = int(left + (right - left)/2)
            cnt = 0
            for num in nums:
                if num <= mid:
                   cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return right

「Floyd 判圈算法」（又称龟兔赛跑算法）
https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode/
"""