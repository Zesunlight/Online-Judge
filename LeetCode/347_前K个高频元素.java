import java.util.*;

/*
    347. 前 K 个高频元素
    https://leetcode-cn.com/problems/top-k-frequent-elements/

    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

    执行用时：17 ms, 在所有 Java 提交中击败了60.76%的用户
    内存消耗：41.3 MB, 在所有 Java 提交中击败了66.96%的用户
 */


class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        Queue<Integer> queue = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if (map.get(o1) < map.get(o2)) return -1;
                else if (map.get(o1) > map.get(o2)) return 1;
                return 0;
            }
        });

        for (Integer i : map.keySet()) {
            if (queue.size() < k) queue.offer(i);
            else if (map.get(i) > map.get(queue.peek())) {
                queue.poll();
                queue.offer(i);
            }
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = queue.poll();
        }
        return result;
    }
}
