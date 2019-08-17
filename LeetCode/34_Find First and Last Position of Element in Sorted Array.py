"""
    Problem: 34. Find First and Last Position of Element in Sorted Array
    Website: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 100 ms, faster than 73.93% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    Memory Usage: 15.1 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""


class Solution:
    """
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].
    """

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        left, right = 0, len(nums) - 1
        middle = (left + right) // 2
        while left <= right:
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                if nums[left] == target:
                    start = left
                    break
                elif nums[left + 1] == target:
                    start = left + 1
                    break
                else:
                    right = middle
                    left += 1

            middle = (left + right) // 2
        else:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        middle = (left + right + 1) // 2
        while left <= right:
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                if nums[right] == target:
                    end = right
                    break
                elif nums[right - 1] == target:
                    end = right - 1
                    break
                else:
                    left = middle
                    right -= 1
            middle = (left + right + 1) // 2
        else:
            return [-1, -1]

        return [start, end]


s = Solution()
a = [0]
b = 0
print(s.searchRange(a, b))


"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14734/Easy-java-O(logn)-solution
simpler solution than my own

public class Solution {
public int[] searchRange(int[] nums, int target) {
    int[] result = new int[2];
    result[0] = findFirst(nums, target);
    result[1] = findLast(nums, target);
    return result;
}

private int findFirst(int[] nums, int target){
    int idx = -1;
    int start = 0;
    int end = nums.length - 1;
    while(start <= end){
        int mid = (start + end) / 2;
        if(nums[mid] >= target){
            end = mid - 1;
        }else{
            start = mid + 1;
        }
        if(nums[mid] == target) idx = mid;
    }
    return idx;
}

private int findLast(int[] nums, int target){
    int idx = -1;
    int start = 0;
    int end = nums.length - 1;
    while(start <= end){
        int mid = (start + end) / 2;
        if(nums[mid] <= target){
            start = mid + 1;
        }else{
            end = mid - 1;
        }
        if(nums[mid] == target) idx = mid;
    }
    return idx;
}
"""

"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)

vector<int> searchRange(int A[], int n, int target) {
    int i = 0, j = n - 1;
    vector<int> ret(2, -1);
    // Search for the left one
    while (i < j)
    {
        int mid = (i + j) /2;
        if (A[mid] < target) i = mid + 1;
        else j = mid;
    }
    if (A[i]!=target) return ret;
    else ret[0] = i;

    // Search for the right one
    j = n-1;  // We don't have to set i to 0 the second time.
    while (i < j)
    {
        int mid = (i + j) /2 + 1;	// Make mid biased to the right
        if (A[mid] > target) j = mid - 1;  
        else i = mid;				// So that this won't make the search range stuck.
    }
    ret[1] = j;
    return ret; 
}
"""

"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14717/C++-binary-search-solution-(lower_bound-implementation).

vector<int> searchRange(vector<int>& nums, int target) {
    int idx1 = lower_bound(nums, target);
    int idx2 = lower_bound(nums, target+1)-1;
    if (idx1 < nums.size() && nums[idx1] == target)
        return {idx1, idx2};
    else
        return {-1, -1};
}

int lower_bound(vector<int>& nums, int target) {
    int l = 0, r = nums.size()-1;
    while (l <= r) {
        int mid = (r-l)/2+l;
        if (nums[mid] < target)
            l = mid+1;
        else
            r = mid-1;
    }
    return l;
}
"""