# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1356. 根据数字二进制下 1 的数目排序
Website: https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 80 ms, 在所有 Python3 提交中击败了11.65%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了15.75%的用户
=================================================="""


class Solution:
    """
    给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
    如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
    请你返回排序后的数组。
    """

    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (self.one(x), x))
        return arr

    def one(self, a):
        n = 0
        while a > 0:
            if a & 1 == 1:
                n += 1
            a = a >> 1
        return n


'''
class Solution {
    public int[] sortByBits(int[] arr) {
        int[] map = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            map[i] = Integer.bitCount(arr[i]) * 10000000 + arr[i];
        }
        Arrays.sort(map);
        for (int i = 0; i < map.length; i++) {
            map[i] = map[i] % 10000000;
        }
        return map;
    }
}

作者：yourtion
链接：https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/solution/javaliang-ci-xun-huan-da-bai-100-by-yourtion/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''