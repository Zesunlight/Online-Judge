"""
    Problem: 26. 删除排序数组中的重复项
    Website: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 56 ms, 在所有 Python3 提交中击败了58.93%的用户
    Memory Usage: 14.7 MB, 在所有 Python3 提交中击败了8.16%的用户
"""

class Solution:
    """
    给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        modify = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                modify = i
                break
        else:
            return len(nums)
        
        for i in range(modify+1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[modify] = nums[i]
                modify += 1
                
        return modify


"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shan-chu-pai-xu-shu-zu-zhong-de-zhong-fu-xiang-by-/

public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
"""
