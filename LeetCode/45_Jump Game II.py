"""
    Problem: 45. Jump Game II
    Website: https://leetcode.com/problems/jump-game-ii/
    Difficulty: Hard
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 6000 ms, faster than 5.02% of Python3 online submissions for Jump Game II.
    Memory Usage: 15 MB, less than 8.33% of Python3 online submissions for Jump Game II.
"""


class Solution:
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Your goal is to reach the last index in the minimum number of jumps.
    """

    def jump(self, nums: List[int]) -> int:
        stride = [0] * len(nums)

        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= len(nums) - 1:
                stride[i] = 1
            elif nums[i] == 0:
                stride[i] = len(nums) + 1
            else:
                stride[i] = min(stride[i + 1: i + nums[i] + 1]) + 1

        return stride[0]


"""
https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy

The main idea is based on greedy. Let's say the range of the current jump is [curBegin, curEnd], curFarthest is the farthest point that all points in [curBegin, curEnd] can reach. Once the current point reaches curEnd, then trigger another jump, and set the new curEnd with curFarthest, then keep the above steps, as the following:

public int jump(int[] A) {
    int jumps = 0, curEnd = 0, curFarthest = 0;
    for (int i = 0; i < A.length - 1; i++) {
        curFarthest = Math.max(curFarthest, i + A[i]);
        if (i == curEnd) {
            jumps++;
            curEnd = curFarthest;
        }
    }
    return jumps;
}

一步跳跃的范围、两步跳跃的范围....
"""


"""
https://leetcode.com/problems/jump-game-ii/discuss/18028/O(n)-BFS-solution

 int jump(int A[], int n) {
     if(n<2)return 0;
     int level=0,currentMax=0,i=0,nextMax=0;

     while(currentMax-i+1>0){       //nodes count of current level>0
         level++;
         for(;i<=currentMax;i++){   //traverse current level , and update the max reach of next level
            nextMax=max(nextMax,A[i]+i);
            if(nextMax>=n-1)return level;   // if last element is in level+1,  then the min jump=level 
         }
         currentMax=nextMax;
     }
     return 0;
 }

广度优先搜索，看最后一个出现在第几层，就跳几步
"""
