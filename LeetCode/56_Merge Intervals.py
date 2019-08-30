"""
    Problem: 56. Merge Intervals
    Website: https://leetcode.com/problems/merge-intervals/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 128 ms, faster than 5.04% of Python3 online submissions for Merge Intervals.
    Memory Usage: 15.4 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
"""


class Solution:
    """
    Given a collection of intervals, merge all overlapping intervals.

    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    """

    def merge(self, intervals):
        res = []
        for i in range(len(intervals)):
            temp = []
            for wait in res:
                if max(wait[0], intervals[i][0]) <= min(wait[1], intervals[i][1]):
                    intervals[i] = [min(wait[0], intervals[i][0]), max(wait[1], intervals[i][1])]
                    # res.remove(wait)
                else:
                    temp.append(wait)
            temp.append(intervals[i])
            res = temp

        return res


s = Solution()
a = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
print(s.merge(a))


"""
https://leetcode.com/problems/merge-intervals/discuss/21222/A-simple-Java-solution

The idea is to sort the intervals by their starting points. 
Then, we take the first interval and compare its end with the next intervals starts. 
As long as they overlap, we update the end to be the max end of the overlapping intervals. 
Once we find a non overlapping interval, we can add the previous "extended" interval and start over.
Sorting takes O(n log(n)) and merging the intervals takes O(n). So, the resulting algorithm takes O(n log(n)).

class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1)
            return intervals;

        // Sort by ascending starting point
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));

        List<int[]> result = new ArrayList<>();
        int[] newInterval = intervals[0];
        result.add(newInterval);
        for (int[] interval : intervals) {
            if (interval[0] <= newInterval[1]) // Overlapping intervals, move the end if needed
                newInterval[1] = Math.max(newInterval[1], interval[1]);
            else {                             // Disjoint intervals, add the new interval to the list
                newInterval = interval;
                result.add(newInterval);
            }
        }

        return result.toArray(new int[result.size()][]);
    }
}
"""

"""
https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python

def merge(self, intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out
"""
