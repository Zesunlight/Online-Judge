# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1470. 重新排列数组
Website: https://leetcode-cn.com/problems/shuffle-the-array/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms
Memory Usage: 14.8 MB
=================================================="""


class Solution:
    """
    给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
    请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
    """
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[i], nums[i+len(nums)//2] for i in range(len(nums)//2)]

    def shuffle(self,nums,n):
        # https://leetcode-cn.com/problems/shuffle-the-array/comments/432517
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums


"""
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {

        for(int i = 0; i < 2 * n; i ++)
            if(nums[i] > 0){
                
                // j 描述当前的 nums[i] 对应的索引，初始为 i
                int j = i; 

                while(nums[i] > 0){

                    // 计算 j 索引的元素，也就是现在的 nums[i]，应该放置的索引
                    j = j < n ? 2 * j : 2 * (j - n) + 1; 

                    // 把 nums[i] 放置到 j 的位置，
                    // 同时，把 nums[j] 放到 i 的位置，在下一轮循环继续处理
                    swap(nums[i], nums[j]); 

                    // 使用负号标记上，现在 j 位置存储的元素已经是正确的元素了 
                    nums[j] = -nums[j]; 
                }
            }

        for(int& e: nums) e = -e;
        return nums;
    }
};

作者：liuyubobobo
链接：https://leetcode-cn.com/problems/shuffle-the-array/solution/kong-jian-fu-za-du-wei-o1-de-liang-chong-jie-fa-by/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
