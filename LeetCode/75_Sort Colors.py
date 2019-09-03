"""
    Problem: 75. Sort Colors
    Website: https://leetcode.com/problems/sort-colors/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 44 ms, faster than 30.60% of Python3 online submissions for Sort Colors.
    Memory Usage: 13.8 MB, less than 6.25% of Python3 online submissions for Sort Colors.
"""


class Solution:
    """
    Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

    Note: You are not suppose to use the library's sort function for this problem.
    """

    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums) - 1)
        print(nums)

    def partition(self, nums, start, end):
        # print('------------------')
        # print(nums, start, end)
        pivot = end
        end -= 1

        while start <= end:
            if nums[start] <= nums[pivot]:
                start += 1
            elif nums[end] > nums[pivot]:
                end -= 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
        else:
            nums[start], nums[pivot] = nums[pivot], nums[start]

        # print(nums, start, end)
        # print('-----------------')
        return start

    def quickSort(self, nums, start, end):
        if end - start <= 0:
            pass
        elif end - start == 1:
            if nums[start] > nums[end]:
                nums[start], nums[end] = nums[end], nums[start]
        else:
            position = self.partition(nums, start, end)
            self.quickSort(nums, start, position - 1)
            self.quickSort(nums, position + 1, end)


s = Solution()
a = [2, 0, 2, 1, 1, 0]


"""
https://leetcode.com/problems/sort-colors/discuss/26472/Share-my-at-most-two-pass-constant-space-10-line-solution
The idea is to sweep all 0s to the left and all 2s to the right, then all 1s are left in the middle.

class Solution {
public:
    void sortColors(int A[], int n) {
        int second=n-1, zero=0;
        for (int i=0; i<=second; i++) {
            while (A[i]==2 && i<second) swap(A[i], A[second--]);
            while (A[i]==0 && i>zero) swap(A[i], A[zero++]);
        }
    }
};

with the same idea
https://leetcode.com/problems/sort-colors/discuss/26474/Sharing-C%2B%2B-solution-with-Good-Explanation
https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
"""

"""
https://leetcode.com/problems/sort-colors/discuss/26500/Four-different-solutions

// two pass O(m+n) space
void sortColors(int A[], int n) {
    int num0 = 0, num1 = 0, num2 = 0;
    
    for(int i = 0; i < n; i++) {
        if (A[i] == 0) ++num0;
        else if (A[i] == 1) ++num1;
        else if (A[i] == 2) ++num2;
    }
    
    for(int i = 0; i < num0; ++i) A[i] = 0;
    for(int i = 0; i < num1; ++i) A[num0+i] = 1;
    for(int i = 0; i < num2; ++i) A[num0+num1+i] = 2;
}

// one pass in place solution
void sortColors(int A[], int n) {
    int n0 = -1, n1 = -1, n2 = -1;
    for (int i = 0; i < n; ++i) {
        if (A[i] == 0) 
        {
            A[++n2] = 2; A[++n1] = 1; A[++n0] = 0;
        }
        else if (A[i] == 1) 
        {
            A[++n2] = 2; A[++n1] = 1;
        }
        else if (A[i] == 2) 
        {
            A[++n2] = 2;
        }
    }
}
"""