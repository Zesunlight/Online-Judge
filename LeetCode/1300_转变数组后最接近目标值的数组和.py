# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1300. 转变数组后最接近目标值的数组和
Website: https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了90.32%的用户
Memory Usage: 14.6 MB, 在所有 Python3 提交中击败了25.00%的用户
=================================================="""


class Solution:
    """
    给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，
    使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
    如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
    请注意，答案不一定是 arr 中的数字。
    """

    def findBestValue(self, arr, target: int) -> int:
        arr.sort()
        s = 0
        res = target
        distance = target
        for i in range(len(arr)):
            poss = (target - s) // (len(arr) - i)
            if i > 0 and poss < arr[i-1]:
                # target is too small
                return 0 if res == target else res
            if poss <= arr[i]:
                temp = abs(poss * (len(arr) - i) + s - target)
                if distance > temp:
                    distance = temp
                    res = poss
            if poss + 1 <= arr[i]:
                temp = abs((poss + 1) * (len(arr) - i) + s - target)
                if distance > temp:
                    distance = temp
                    res = poss + 1
            s += arr[i]
        if res == target:
            # target is too large
            res = arr[-1]
        return res


s = Solution()
print(s.findBestValue(arr = [4,9,3], target = 10))

"""
ans 的下界为 0，上届为 max(arr)
枚举 + 二分查找

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        
        r, ans, diff = max(arr), 0, target
        for i in range(1, r + 1):
            it = bisect.bisect_left(arr, i)
            cur = prefix[it] + (n - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/solution/bian-shu-zu-hou-zui-jie-jin-mu-biao-zhi-de-shu-zu-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

"""
int cmp(const void* c1, const void* c2) {
    return *(int*)c1 - *(int*)c2;
}

int findBestValue(int* arr, int arrSize, int target){
    if (arr == NULL) {
        return 0;
    }
    qsort(arr, arrSize, sizeof(int), cmp);
    int sum = 0;
    for (int i = 0; i < arrSize; i++) {
        int x = (target - sum) / (arrSize - i);
        if (x < arr[i]) {
            double t = ((double)(target - sum))/(arrSize - i);
            if (t - x > 0.5) {
                return x + 1;
            } else {
                return x;
            }
        }
        sum += arr[i];
    }
    return arr[arrSize - 1];
}

作者：hai-tun-da-ren
链接：https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/solution/zhe-ci-guan-fang-de-jie-fa-gan-jue-fu-za-liao-shua/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""