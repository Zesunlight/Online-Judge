"""
    Problem: 57. 插入区间
    Website: https://leetcode-cn.com/problems/insert-interval/
    Difficulty: 困难
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 60 ms, faster than 16.47% of Python3 online submissions for Merge Intervals.
    Memory Usage: 15.2 MB, less than 5.07% of Python3 online submissions for Merge Intervals.
"""

"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        from bisect import bisect_left
        idx = bisect_left([i[0] for i in intervals], newInterval[0])
        drop = [idx, idx]
        insert = idx
        
        if idx > 0:
            if newInterval[0] <= intervals[idx - 1][1]:
                newInterval[0] = intervals[idx - 1][0]
                newInterval[1] = max(newInterval[1], intervals[idx - 1][1])
                drop[0] = idx - 1
                drop[1] = idx
                insert = idx - 1
        while idx < len(intervals) and newInterval[1] >= intervals[idx][0]:
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
            drop[1] = idx
        
        result = intervals[:drop[0]]
        result.extend(intervals[drop[1]:])
        result.insert(insert, newInterval)
        return result


class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)
        
        if not placed:
            ans.append([left, right])
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/insert-interval/solution/cha-ru-qu-jian-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。