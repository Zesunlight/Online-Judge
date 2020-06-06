# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 128. 最长连续序列
Website: https://leetcode-cn.com/problems/longest-consecutive-sequence/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了40.45%的用户
Memory Usage: 14.7 MB, 在所有 Python3 提交中击败了8.33%的用户
=================================================="""


class Solution:
    """
    给定一个未排序的整数数组，找出最长连续序列的长度。

    要求算法的时间复杂度为 O(n)。
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) <= 1:
            return len(nums)
        l = 1
        for i in nums:
            if (i - 1 in nums) or (i + 1 not in nums):
                continue
            temp = i
            curr = 1
            while temp + 1 in nums:
                curr += 1
                temp += 1
            l = max(l, curr)
        return l

"""
https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
"""

"""
class Solution {
public:
    unordered_map<int,int> a,b;
    int find(int x){
        return a.count(x)?a[x]=find(a[x]):x;
    }
    int longestConsecutive(vector<int>& nums) {
        for(auto i:nums)
            a[i]=i+1;
        int ans=0;
        for(auto i:nums){
            int y=find(i+1);
            ans=max(ans,y-i);
        }
        return ans;
    }
};

作者：leck
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/cbing-cha-ji-xie-fa-dai-ma-ji-duan-by-leck/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""