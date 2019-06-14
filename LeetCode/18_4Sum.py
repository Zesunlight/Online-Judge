class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        res = []
        if len(nums) < 4 or target > nums[-1] * 4:
            return res

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            goal_1 = target - nums[i]
            if goal_1 < nums[i + 1] * 3:
                break
            if goal_1 > nums[-1] * 3:
                continue

            for j in range(i + 1, len(nums) - 2):
                goal_2 = goal_1 - nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                third = j + 1
                forth = len(nums) - 1
                while third < forth:
                    if nums[third] + nums[forth] < goal_2:
                        third += 1
                    elif nums[third] + nums[forth] > goal_2:
                        forth -= 1
                    else:
                        res.append([nums[i], nums[j], nums[third], nums[forth]])
                        while third + 1 < forth and nums[third] == nums[third + 1]:
                            third += 1
                        while third < forth - 1 and nums[forth] == nums[forth - 1]:
                            forth -= 1

                        third += 1
                        forth -= 1

        return res


a = Solution()
print(a.fourSum([-1, 0, 1, 2, -1, -4, 4, -1, 0, 1, 2, -1, -4, 4, -1, 0, 1, 2, -1, -4, 4, -1, 0, 1, 2, -1, -4, 4], 0))

'''
the same thoughts as 3Sum
'''