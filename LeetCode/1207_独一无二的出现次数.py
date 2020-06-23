# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1207. 独一无二的出现次数
Website: https://leetcode-cn.com/problems/unique-number-of-occurrences/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了44.43%的用户
Memory Usage: 13.8 MB, 在所有 Python3 提交中击败了11.11%的用户
=================================================="""


class Solution:
    """
    给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

    如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        if len(set(c.values())) == len(c):
            return True
        return False


"""
class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        Set<Integer> set = new HashSet<Integer>();
        
        // 记录出现次数
        for(int data :arr) {
            map.put(a, map.getOrDefault(a, 0) + 1);
        }
        
        // 验证重复值
        for(Integer i : map.values()) {
            if (!set.add(i)) return false;
        }
        return true;
    }
}

作者：Magic
链接：https://leetcode-cn.com/problems/unique-number-of-occurrences/solution/java-shi-jian-kong-jian-100hashmaphashset-by-magic/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""