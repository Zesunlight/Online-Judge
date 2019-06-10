class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range(len(nums)):

            # remove duplicate number on the first position
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            target = -nums[i]
            start = i + 1
            end = len(nums) - 1

            while start < end:
                if nums[start] + nums[end] < target:
                    start += 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    res.append([nums[i], nums[start], nums[end]])

                    # remove duplicate number on the second position
                    while (start + 1 < end) and (nums[start + 1] == nums[start]):
                        start += 1
                    # remove duplicate number on the third position
                    while (start < end - 1) and (nums[end - 1] == nums[end]):
                        end -= 1

                    start += 1
                    end -= 1

        return res

a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4, 4]))

'''
https://leetcode.com/problems/3sum/discuss/7402/Share-my-AC-C++-solution-around-50ms-O(N*N)-with-explanation-and-comments
'''