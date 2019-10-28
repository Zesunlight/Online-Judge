## 题目

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

## 例子

> 示例 1:  

> 输入: nums = [4,5,6,7,0,1,2], target = 0 

> 输出: 4



> 示例 2:  

> 输入: nums = [4,5,6,7,0,1,2], target = 3 

> 输出: -1

## 思路

- 二分查找的思想
- 中间的数若大于左边的数，则左半部分是有序的
- 中间的数若小于右边的数，则右半部分是有序的
- 再判断 target 位于那一边，更新 left 或者 right  
- 整体变为有序的
- 旋转的点将数组分成了两个有序的部分
- 中间的数和 target 如果在同一部分，直接更新 left 或者 right
- 如果在不同部分，将中间的数置为 -inf 或者 inf

## 代码

Python（[源码](https://github.com/Zesunlight/Online-Judge/blob/master/LeetCode/33_Search in Rotated Sorted Array.py)）

```python
def search(self, nums, target: int) -> int:
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
```



C++（[参考他人解答](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple)）

```c++
// https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
int search(vector<int>& nums, int target) {
    int lo = 0, hi = nums.size();
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        
        double num = (nums[mid] < nums[0]) == (target < nums[0])
                   ? nums[mid]
                   : target < nums[0] ? -INFINITY : INFINITY;
                   
        if (num < target)
            lo = mid + 1;
        else if (num > target)
            hi = mid;
        else
            return mid;
    }
    return -1;
}
```

## 参考

- [Search in Rotated Sorted Array - LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [搜索旋转排序数组 - 力扣（LeetCode）](https://leetcode-cn.com/problems/search-in-rotated-sorted-array)
- [Online-Judge/33_Search in Rotated Sorted Array.py at master · Zesunlight/Online-Judge](https://github.com/Zesunlight/Online-Judge/blob/master/LeetCode/33_Search in Rotated Sorted Array.py)
- [[LeetCode\] 33. Search in Rotated Sorted Array 在旋转有序数组中搜索 - Grandyang - 博客园](https://www.cnblogs.com/grandyang/p/4325648.html)
- [Clever idea making it simple - LeetCode Discuss](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple)
- [The -INF and INF method but with a better explanation for dummies like me - LeetCode Discuss](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/154836/The-INF-and-INF-method-but-with-a-better-explanation-for-dummies-like-me)