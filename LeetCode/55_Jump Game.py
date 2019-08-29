"""
    Problem: 55. Jump Game
    Website: https://leetcode.com/problems/jump-game/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 104 ms, faster than 64.59% of Python3 online submissions for Jump Game.
    Memory Usage: 15.9 MB, less than 7.14% of Python3 online submissions for Jump Game.
"""


class Solution:
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.
    """

    def canJump(self, nums) -> bool:
        if len(nums) == 1:
            return True

        far = -1
        for i in range(len(nums) - 1):
            far = max(far, nums[i] + i)
            if far < i + 1:
                return False

        return True


s = Solution()
a = [3, 2, 1, 0, 4]
print(s.canJump(a))


"""
https://leetcode.com/problems/jump-game/discuss/20917/Linear-and-simple-solution-in-C++

bool canJump(int A[], int n) {
    int i = 0;
    for (int reach = 0; i < n && i <= reach; ++i)
        reach = max(i + A[i], reach);
    return i == n;
}
"""


"""
https://leetcode.com/problems/jump-game/discuss/20900/Simplest-O(N)-solution-with-constant-space
Idea is to work backwards from the last index. 
Keep track of the smallest index that can "jump" to the last index. 
Check whether the current index can jump to this smallest index.

bool canJump(int A[], int n) {
    int last=n-1,i,j;
    for(i=n-2;i>=0;i--){
        if(i+A[i]>=last)last=i;
    }
    return last<=0;
}
"""
