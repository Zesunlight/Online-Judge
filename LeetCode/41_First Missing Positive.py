"""
    Problem: 41. First Missing Positive
    Website: https://leetcode.com/problems/first-missing-positive/
    Difficulty: Hard
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 40 ms, faster than 84.91% of Python3 online submissions for First Missing Positive.
    Memory Usage: 13.8 MB, less than 8.70% of Python3 online submissions for First Missing Positive.
"""


class Solution:
    """
    Given an unsorted integer array, find the smallest missing positive integer.
    """

    def firstMissingPositive(self, nums) -> int:
        if not nums:
            return 1

        nums.sort()
        miss = 1
        for i in range(len(nums) - 1):
            if nums[i] <= 0:
                continue
            elif nums[i] == miss:
                if nums[i + 1] > miss:
                    miss += 1
                else:
                    continue
            else:
                break
        else:
            if nums[-1] == miss:
                miss += 1

        return miss


s = Solution()
a = []
print(s.firstMissingPositive(a))


"""
https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode/
使用索引作为哈希键 以及 元素的符号作为哈希值 来实现是否存在的检测

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # 基本情况
        if 1 not in nums:
            return 1
        
        # nums = [1]
        if n == 1:
            return 2
        
        # 用 1 替换负数，0，
        # 和大于 n 的数
        # 在转换以后，nums 只会包含
        # 正数
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # 使用索引和数字符号作为检查器
        # 例如，如果 nums[1] 是负数表示在数组中出现了数字 `1`
        # 如果 nums[2] 是正数 表示数字 2 没有出现
        for i in range(n): 
            a = abs(nums[i])
            # 如果发现了一个数字 a - 改变第 a 个元素的符号
            # 注意重复元素只需操作一次
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # 现在第一个正数的下标
        # 就是第一个缺失的数
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1
"""

"""
https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c++-solution-O(1)-space-and-O(n)-time
把每个数放到正确的位置上，nums[i] = i+1 是理想情况

class Solution
{
public:
    int firstMissingPositive(int A[], int n)
    {
        for(int i = 0; i < n; ++ i)
            while(A[i] > 0 && A[i] <= n && A[A[i] - 1] != A[i])
                swap(A[i], A[A[i] - 1]);
        
        for(int i = 0; i < n; ++ i)
            if(A[i] != i + 1)
                return i + 1;
        
        return n + 1;
    }
};
"""