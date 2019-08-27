"""
    Problem: 53. Maximum Subarray
    Website: https://leetcode.com/problems/maximum-subarray/
    Difficulty: Easy
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 72 ms, faster than 92.52% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 14.4 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
"""


class Solution:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.

    If you have figured out the O(n) solution,
    try coding another solution using the divide and conquer approach, which is more subtle.
    """

    def maxSubArray(self, nums) -> int:
        res = current = nums[0]

        for n in nums[1:]:
            # current = 结尾为n的最大子数组和
            current = max(current + n, n)
            res = max(current, res)

        return res


s = Solution()
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(a))


"""
https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way

for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)
"""

"""
https://github.com/grandyang/leetcode/issues/53
分治法的思想就类似于二分搜索法，我们需要把数组一分为二，分别找出左边和右边的最大子数组之和，
然后还要从中间开始向左右分别扫描，求出的最大值分别和左右两边得出的最大值相比较取最大的那一个

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.empty()) return 0;
        return helper(nums, 0, (int)nums.size() - 1);
    }
    int helper(vector<int>& nums, int left, int right) {
        if (left >= right) return nums[left];
        int mid = left + (right - left) / 2;
        int lmax = helper(nums, left, mid - 1);
        int rmax = helper(nums, mid + 1, right);
        int mmax = nums[mid], t = mmax;
        for (int i = mid - 1; i >= left; --i) {
            t += nums[i];
            mmax = max(mmax, t);
        }
        t = mmax;
        for (int i = mid + 1; i <= right; ++i) {
            t += nums[i];
            mmax = max(mmax, t);
        }
        return max(mmax, max(lmax, rmax));
    }
};
"""