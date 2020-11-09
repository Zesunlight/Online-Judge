# -*- coding: UTF-8 -*-
"""=================================================
Problem: 973. 最接近原点的 K 个点
Website: https://leetcode-cn.com/problems/k-closest-points-to-origin/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 876 ms, 在所有 Python3 提交中击败了38.30%的用户
Memory Usage: 19.1 MB, 在所有 Python3 提交中击败了18.00%的用户
=================================================="""


class Solution:
    """
    给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
    """
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        close = []
        for i in range(len(points)):
            heapq.heappush(close, Test(points[i]))
        return [heapq.heappop(close).points for _ in range(K)]


class Test:
    def __init__(self, p):
        self.points = p
        self.distance = math.hypot(p[0], p[1])

    def __lt__(self, other):
        return self.distance < other.distance


class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/k-closest-points-to-origin/solution/zui-jie-jin-yuan-dian-de-k-ge-dian-by-leetcode-sol/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 计算欧几里得距离
        distance = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        
        def work(i, j, K):
            if i > j:
                return
            # 记录初始值
            oi, oj = i, j
            # 取最左边为哨兵值
            pivot = distance(oi)
            while i != j:
                while i < j and distance(j) >= pivot:
                    j -= 1
                while i < j and distance(i) <= pivot:
                    i += 1
                if i < j:
                    # 交换值
                    points[i], points[j] = points[j], points[i] 
                
            # 交换哨兵
            points[i], points[oi] = points[oi], points[i]
            
            # 递归
            if K <= i - oi + 1:
                # 左半边排序
                work(oi, i - 1, K)
            else:
                # 右半边排序
                work(i + 1, oj, K - (i - oi + 1))
                
        work(0, len(points) - 1, K)
        return points[:K]

# 作者：jalan
# 链接：https://leetcode-cn.com/problems/k-closest-points-to-origin/solution/tou-lan-yu-kuai-pai-by-jalan/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



"""
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(new Comparator<int[]>() {
            public int compare(int[] array1, int[] array2) {
                return array2[0] - array1[0];
            }
        });
        for (int i = 0; i < K; ++i) {
            pq.offer(new int[]{points[i][0] * points[i][0] + points[i][1] * points[i][1], i});
        }
        int n = points.length;
        for (int i = K; i < n; ++i) {
            int dist = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            if (dist < pq.peek()[0]) {
                pq.poll();
                pq.offer(new int[]{dist, i});
            }
        }
        int[][] ans = new int[K][2];
        for (int i = 0; i < K; ++i) {
            ans[i] = points[pq.poll()[1]];
        }
        return ans;

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/k-closest-points-to-origin/solution/zui-jie-jin-yuan-dian-de-k-ge-dian-by-leetcode-sol/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    }

    public int[][] kClosest(int[][] points, int K) {
        // https://leetcode-cn.com/problems/k-closest-points-to-origin/solution/zui-jie-jin-yuan-dian-de-k-ge-dian-by-leetcode-sol/659252
        Arrays.sort(points, Comparator.comparingInt((array) -> array[0] * array[0] + array[1] * array[1]));
        return Arrays.copyOf(points, K);
    }
}
"""