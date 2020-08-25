/*
=================================================
Problem: 面试题 56 - I. 数组中数字出现的次数
Website: https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
Difficulty: 中等
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 2 ms, 在所有 Java 提交中击败了97.20%的用户
Memory Usage: 41.4 MB, 在所有 Java 提交中击败了51.76%的用户
==================================================*/


class Solution {
    public int[] singleNumbers(int[] nums) {
        int n = nums.length;
        if (n == 2) return nums;
        int xor = nums[0];
        for (int i = 1; i < n; i++) {
            xor ^= nums[i];
        }

        int idx = 1;
        while ((xor & idx) == 0) {
            idx <<= 1;
        }

        int first = idx, second = 0;
        for (int num : nums) {
            if ((num & idx) == 0) {
                second ^= num;
            } else {
                first ^= num;
            }
        }
        first ^= idx;
        second ^= 0;

        return new int[] {first, second};
    }
}


class Solution2 {
    public int[] singleNumbers(int[] nums) {
        int sum = 0;
        int[] res = new int[2];
        for(int num : nums){
            sum ^= num;
        }
        int lowbit = sum & (-sum);
        for(int num : nums){
            if((num & lowbit) == 0){
                res[0] ^= num;
            }else{
                res[1] ^= num;
            }
        }
        return res;
    }
}
// https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-by-leetcode/371027


/*
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/