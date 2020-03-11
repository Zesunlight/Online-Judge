## 题目

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array

## 例子

### 示例 1: 

> ```
> 输入: nums = [5,7,7,8,8,10], target = 8
> 输出: [3,4]
> ```

### 示例 2: 

> ```
> 输入: nums = [5,7,7,8,8,10], target = 6
> 输出: [-1,-1]
> ```

## 思路

- 做两遍二分查找，分别找到开始位置和结束位置
- 注意条件的选择，边界的判断

## 代码

Python

```python
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
```

想的确实麻烦了，有更简洁的表达



Java（[参考他人解答](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple)）

```java
// https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
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
```

## 参考

- [Find First and Last Position of Element in Sorted Array - LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [在排序数组中查找元素的第一个和最后一个位置 - 力扣（LeetCode）](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [Online-Judge/34_Find First and Last Position of Element in Sorted Array.py at master · Zesunlight/Online-Judge](https://github.com/Zesunlight/Online-Judge/blob/master/LeetCode/34_Find First and Last Position of Element in Sorted Array.py)
- [Easy java O(logn) solution - LeetCode Discuss](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14734/Easy-java-O(logn)-solution
)
- [Clean iterative solution with two binary searches (with explanation) - LeetCode Discuss](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)
)
- [C++ binary search solution (lower_bound implementation). - LeetCode Discuss](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14717/C++-binary-search-solution-(lower_bound-implementation).
) 
