import java.util.*;

/*
    16. 最接近的三数之和
    https://leetcode-cn.com/problems/3sum-closest/

    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。

    执行用时：9 ms, 在所有 Java 提交中击败了26.90%的用户
    内存消耗：39.5 MB, 在所有 Java 提交中击败了6.82%的用户
 */

class Solution {
    public static int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int start = 0, left = 1, right = nums.length - 1;
        int res = nums[start] + nums[left] + nums[right] - target;
        for (; start < nums.length - 2; start++) {
            left = start + 1;
            right = nums.length - 1;
            while (left < right) {
                int temp = nums[start] + nums[left] + nums[right] - target;
                if (Math.abs(temp) < Math.abs(res)) {
                    res = temp;
                }
                if (temp < 0) {
                    left++;
                } else if (temp > 0) {
                    right--;
                } else {
                    return target;
                }
            }
        }
        return target + res;
    }

    public static void main(String[] args) {
        int[] nums = {-1,2,1,-4};
        System.out.println(threeSumClosest(nums, 1));
    }
}


class Solution2 {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int best = 10000000;

        // 枚举 a
        for (int i = 0; i < n; ++i) {
            // 保证和上一次枚举的元素不相等
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            // 使用双指针枚举 b 和 c
            int j = i + 1, k = n - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                // 如果和为 target 直接返回答案
                if (sum == target) {
                    return target;
                }
                // 根据差值的绝对值来更新答案
                if (Math.abs(sum - target) < Math.abs(best - target)) {
                    best = sum;
                }
                if (sum > target) {
                    // 如果和大于 target，移动 c 对应的指针
                    int k0 = k - 1;
                    // 移动到下一个不相等的元素
                    while (j < k0 && nums[k0] == nums[k]) {
                        --k0;
                    }
                    k = k0;
                } else {
                    // 如果和小于 target，移动 b 对应的指针
                    int j0 = j + 1;
                    // 移动到下一个不相等的元素
                    while (j0 < k && nums[j0] == nums[j]) {
                        ++j0;
                    }
                    j = j0;
                }
            }
        }
        return best;
    }
}

//作者：LeetCode-Solution
//链接：https://leetcode-cn.com/problems/3sum-closest/solution/zui-jie-jin-de-san-shu-zhi-he-by-leetcode-solution/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。