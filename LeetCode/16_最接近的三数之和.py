# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 16. 最接近的三数之和
Website: https://leetcode-cn.com/problems/3sum-closest/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 116 ms, 在所有 Python3 提交中击败了70.91%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了9.38%的用户
=================================================="""


class Solution:
    """
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。
    """
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        gap = sum(nums[:3]) - target
        if gap >= 0:
            return gap + target
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current = nums[left] + nums[right] + nums[i]
                temp = current - target
                if current > target:
                    right -= 1
                    if abs(gap) > temp:
                        gap = temp
                elif current < target:
                    left += 1
                    if abs(gap) > -temp:
                        gap = temp
                else:
                    return target
        return target + gap


s = Solution()
print(s.threeSumClosest([-3, 2, 1, 0], 1))

"""
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int ans = nums[0] + nums[1] + nums[2];
        for(int i=0;i<nums.length;i++) {
            int start = i+1, end = nums.length - 1;
            while(start < end) {
                int sum = nums[start] + nums[end] + nums[i];
                if(Math.abs(target - sum) < Math.abs(target - ans))
                    ans = sum;
                if(sum > target)
                    end--;
                else if(sum < target)
                    start++;
                else
                    return ans;
            }
        }
        return ans;
    }
}

作者：guanpengchn
链接：https://leetcode-cn.com/problems/3sum-closest/solution/hua-jie-suan-fa-16-zui-jie-jin-de-san-shu-zhi-he-b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
