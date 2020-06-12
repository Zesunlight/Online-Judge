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

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''