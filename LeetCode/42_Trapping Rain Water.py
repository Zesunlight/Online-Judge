"""
    Problem: 42. Trapping Rain Water
    Website: https://leetcode.com/problems/trapping-rain-water/
    Difficulty: Hard
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 56 ms, faster than 90.14% of Python3 online submissions for Trapping Rain Water.
    Memory Usage: 14.5 MB, less than 6.98% of Python3 online submissions for Trapping Rain Water.
"""


class Solution:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it is able to trap after raining.
    """

    def trap(self, height) -> int:
        if len(height) <= 2:
            return 0
        local_max = []
        rain = 0
        height.append(0)
        if height[0] > height[1]:
            local_max.append(0)

        for i in range(1, len(height) - 1):
            if (height[i] >= height[i + 1]) and (height[i] >= height[i - 1]):
                if len(local_max) == 0:
                    local_max.append(i)
                    continue
                else:
                    if height[i] >= height[local_max[0]]:
                        local_max.append(i)
                        rain += self.fill(height, local_max)
                        local_max.clear()
                        local_max.append(i)
                    else:
                        while len(local_max) > 1:
                            if height[local_max[-1]] <= height[i]:
                                local_max.pop()
                            else:
                                local_max.append(i)
                                break
                        else:
                            local_max.append(i)

        if len(local_max) >= 2:
            rain += self.fill(height, local_max)
        return rain

    def fill(self, height, leap):
        print(leap)
        volume = 0
        if height[leap[-1]] >= height[leap[0]]:
            start = leap[0]
            end = leap[-1]
            for tiny in range(start + 1, end):
                if height[start] - height[tiny] >= 0:
                    volume += height[start] - height[tiny]
                else:
                    break
        else:
            for position in range(len(leap) - 1, 0, -1):
                end = leap[position]
                start = leap[position - 1]
                for tiny in range(end - 1, start, -1):
                    if height[end] - height[tiny] >= 0:
                        volume += height[end] - height[tiny]
                    else:
                        break
        print(volume)
        return volume


s = Solution()
a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
a = [1, 0, 3, 4, 0, 1]
a = [5, 2, 1, 2, 1, 5]
a = [9, 6, 8, 8, 5, 6, 3]
print(s.trap(a))


"""
https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c++-code:-O(n)-time-O(1)-space

Here is my idea: instead of calculating area by height*width, we can think it in a cumulative way. 
In other words, sum water amount of each bin(width=1).
Search from left to right and maintain a max height of left and right separately, 
which is like a one-side wall of partial container. 
Fix the higher one and flow water from the lower part. 
For example, if current height of left is lower, we fill water in the left bin. 
Until left meets right, we filled the whole container.

class Solution {
public:
    int trap(int A[], int n) {
        int left=0; int right=n-1;
        int res=0;
        int maxleft=0, maxright=0;
        while(left<=right){
            if(A[left]<=A[right]){
                if(A[left]>=maxleft) maxleft=A[left];
                else res+=maxleft-A[left];
                left++;
            }
            else{
                if(A[right]>=maxright) maxright= A[right];
                else res+=maxright-A[right];
                right--;
            }
        }
        return res;
    }
};
"""

"""
https://leetcode.com/problems/trapping-rain-water/discuss/17386/Sharing-my-Java-code:-O(n)-time-O(1)-space

Traverse one pass with two pointers, from two sides to the middle.

public int trap(int[] A) {
    if (A.length < 3) return 0;
    
    int ans = 0;
    int l = 0, r = A.length - 1;
    
    // find the left and right edge which can hold water
    while (l < r && A[l] <= A[l + 1]) l++;
    while (l < r && A[r] <= A[r - 1]) r--;
    
    while (l < r) {
        int left = A[l];
        int right = A[r];
        if (left <= right) {
            // add volum until an edge larger than the left edge
            while (l < r && left >= A[++l]) {
                ans += left - A[l];
            }
        } else {
            // add volum until an edge larger than the right volum
            while (l < r && A[--r] <= right) {
                ans += right - A[r];
            }
        }
    }
    return ans;
}
"""
