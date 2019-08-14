"""
    Problem: 33. Search in Rotated Sorted Array
    Website: https://leetcode.com/problems/search-in-rotated-sorted-array/
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 68 ms, faster than 5.97% of Python3 online submissions for Search in Rotated Sorted Array.
    Memory Usage: 14 MB, less than 6.29% of Python3 online submissions for Search in Rotated Sorted Array.
"""


class Solution:
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Your algorithm's runtime complexity must be in the order of O(log n).
    """

    def search(self, nums, target: int) -> int:
        # reference: https://www.cnblogs.com/grandyang/p/4325648.html

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle

            if nums[middle] < nums[right]:
                # nums[middle:right+1] is ascending

                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                elif target < nums[middle] or nums[right] < target:
                    right = middle - 1
            else:
                # nums[left:middle+1] is ascending
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                elif target < nums[left] or nums[middle] < target:
                    left = middle + 1

        return -1


s = Solution()
a = [4, 5, 6, 7, 0, 1, 2]
b = 3
print(s.search(a, b))


"""
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple

Explanation

Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

If target is let's say 7, then we adjust nums to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

And then we can simply do ordinary binary search.

Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at. 
And the adjustment is done by comparing both the target and the actual element against nums[0].

https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/154836/The-INF-and-INF-method-but-with-a-better-explanation-for-dummies-like-me
分成两个部分，这两个部分都是升序的

class Solution {
public:
    int search(vector<int>& nums, int target) 
    {
            int l = 0, r = nums.size()-1;
            while(l <= r)
            {
                int mid = (r - l)/2 + l;
                int comparator = nums[mid];
                // Checking if both target and nums[mid] are on same side.
                if((target < nums[0]) && (nums[mid] < nums[0]) || (target >= nums[0]) && (nums[mid] >= nums[0]))
                    comparator = nums[mid];
                else
                {
                    // Trying to figure out where nums[mid] is and making comparator as -INF or INF
                    if(target <nums[0])
                        comparator = -INFINITY;
                    else 
                        comparator = INFINITY;

                }
                if(target == comparator) return mid;
                if(target > comparator)            
                    l = mid+1;            
                else
                    r = mid-1;

            }
            return -1;
    }
};
"""