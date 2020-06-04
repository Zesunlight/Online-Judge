# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 238. 除自身以外数组的乘积
Website: https://leetcode-cn.com/problems/product-of-array-except-self/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 68 ms, 在所有 Python3 提交中击败了44.36%的用户
Memory Usage: 19.8 MB, 在所有 Python3 提交中击败了9.09%的用户
=================================================="""


class Solution:
    """
    给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

    提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
    说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [nums[0] for _ in range(length)]
        right = [nums[-1] for _ in range(length)]
        for i in range(1, length):
            left[i] = nums[i] * left[i - 1]
        for i in range(length - 2, -1, -1):
            right[i] = nums[i] * right[i + 1]
        res = [0 for _ in range(length)]
        res[0] = right[1]
        res[-1] = left[-2]
        for i in range(1, length - 1):
            res[i] = left[i-1] * right[i+1]
        return res


"""
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] answer = new int[length];

        // answer[i] 表示索引 i 左侧所有元素的乘积
        // 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
        answer[0] = 1;
        for (int i = 1; i < length; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }

        // R 为右侧所有元素的乘积
        // 刚开始右边没有元素，所以 R = 1
        int R = 1;
        for (int i = length - 1; i >= 0; i--) {
            // 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
            answer[i] = answer[i] * R;
            // R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
            R *= nums[i];
        }
        return answer;
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/product-of-array-except-self/solution/chu-zi-shen-yi-wai-shu-zu-de-cheng-ji-by-leetcode-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""