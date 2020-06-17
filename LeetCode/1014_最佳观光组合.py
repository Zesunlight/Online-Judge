# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1014. 最佳观光组合
Website: https://leetcode-cn.com/problems/best-sightseeing-pair/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 772 ms, 在所有 Python3 提交中击败了12.86%的用户
Memory Usage: 18.8 MB, 在所有 Python3 提交中击败了9.09%的用户
=================================================="""


class Solution:
    """
    给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

    一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

    返回一对观光景点能取得的最高分。
    """
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        m = A[0] + 0
        for i in range(1, len(A)):
            m = max(m, A[i-1] + i-1)
            res = max(res, m + A[i] - i)
                
        return res

    def maxScoreSightseeingPair_2(self, A: List[int]) -> int:
        buff = A[0] # 初始buff
        ans = 0
        for j in range(1, len(A)):
            # 随着时间推移，buff的效力不断减少
            # 初始效力为某个A[i], i < j
            # 随时间减少的效力正好为 j - i
            # 因此当前buff的剩余效力恰为 A[i] + i - j
            buff -= 1
            # 根据当前buff默默算一下自己的战斗力（战5渣..)
            ans = max(ans, A[j] + buff)
            # 看看当前buff剩余效力有没有刷新buff好，没有则刷新buff
            buff = max(buff, A[j])
        return ans
    '''
    作者：dan-huang-jiang-xing-ren
    链接：https://leetcode-cn.com/problems/best-sightseeing-pair/solution/lai-lai-lai-gei-zi-ji-jia-ge-buff-by-dan-huang-jia/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''

'''
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int ans = 0, mx = A[0] + 0;
        for (int j = 1; j < A.size(); ++j) {
            ans = max(ans, mx + A[j] - j);
            // 边遍历边维护
            mx = max(mx, A[j] + j);
        }
        return ans;
    }
};

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/best-sightseeing-pair/solution/zui-jia-guan-guang-zu-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''