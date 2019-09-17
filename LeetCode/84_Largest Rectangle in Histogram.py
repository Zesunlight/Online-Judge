"""
    Problem: 84. Largest Rectangle in Histogram
    Website: https://leetcode.com/problems/largest-rectangle-in-histogram/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 128 ms, faster than 44.57% of Python3 online submissions for Largest Rectangle in Histogram.
    Memory Usage: 15.6 MB, less than 9.09% of Python3 online submissions for Largest Rectangle in Histogram.
"""


class Solution:
    """
    Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
    find the area of largest rectangle in the histogram.
    """

    def largestRectangleArea(self, heights) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]

        # Time Limit Exceeded
        # res = [0 for i in range(len(heights))]
        # res[0] = heights[0]
        #
        # for i in range(1, len(heights)):
        #     res[i] = heights[i]
        #     explore = i - 1
        #     micro = heights[i]
        #     while explore >= 0:
        #         if heights[explore] < micro:
        #             micro = heights[explore]
        #         if micro * (i + 1) <= res[i]:
        #             break
        #         res[i] = max(micro * (i - explore + 1), res[i])
        #         explore -= 1
        #     res[i] = max(res[i - 1], res[i])
        #
        # return res[-1]

        ascending = []
        res = 0
        heights.append(0)
        for i in range(len(heights)):
            while ascending and heights[i] < heights[ascending[-1]]:
                temp = ascending.pop()
                res = max(res, heights[temp] * ((i - ascending[-1] - 1) if ascending else i))
            else:
                ascending.append(i)

        return res


s = Solution()
a = [2, 1, 2]
a = [2, 1, 5, 6, 2, 3]
a = [1, 2, 2]
a = [4, 2, 0, 3, 2, 5]
print(s.largestRectangleArea(a))

"""
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/comments/73308
把这个想象成锯木板，如果木板都是递增的那我很开心，如果突然遇到一块木板i矮了一截，那我就先找之前最戳出来的一块（其实就是第i-1块），
计算一下这个木板单独的面积，然后把它锯成次高的，这是因为我之后的计算都再也用不着这块木板本身的高度了。
再然后如果发觉次高的仍然比现在这个i木板高，那我继续单独计算这个次高木板的面积（应该是第i-1和i-2块），再把它俩锯短。
直到发觉不需要锯就比第i块矮了，那我继续开开心心往右找更高的。当然为了避免到了最后一直都是递增的，所以可以在最后加一块高度为0的木板。
"""

"""
https://github.com/grandyang/leetcode/issues/84
遍历数组，每找到一个局部峰值（只要当前的数字大于后面的一个数字，那么当前数字就看作一个局部峰值，跟前面的数字大小无关），
然后向前遍历所有的值，算出共同的矩形面积，每次对比保留最大值。非局部峰值处的情况，后面的局部峰值都可以包括。

class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        int res = 0;
        for (int i = 0; i < height.size(); ++i) {
            if (i + 1 < height.size() && height[i] <= height[i + 1]) {
                continue;
            }
            int minH = height[i];
            for (int j = i; j >= 0; --j) {
                minH = min(minH, height[j]);
                int area = minH * (i - j + 1);
                res = max(res, area);
            }
        }
        return res;
    }
};


维护一个递增栈，单调栈中不能放高度，而是需要放坐标。
在高度数组最后面加上一个0，这样原先的最后一个板子也可以被处理了。
由于我们先取出栈中最高的板子，那么就可以先算出长度为1的矩形面积了，然后再取下一个板子，此时根据矮板子的高度算长度为2的矩形面积，
以此类推，直到数字大于栈顶元素为止，再次进栈

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = 0;
        stack<int> st;
        heights.push_back(0);
        for (int i = 0; i < heights.size(); ++i) {
            while (!st.empty() && heights[st.top()] >= heights[i]) {
                int cur = st.top(); st.pop();
                res = max(res, heights[cur] * (st.empty() ? i : (i - st.top() - 1)));
            }
            st.push(i);
        }
        return res;
    }
};
"""

"""
https://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
"""
