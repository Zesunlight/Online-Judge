"""
    Problem: 39. Combination Sum
    Website: https://leetcode.com/problems/combination-sum/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 124 ms, faster than 27.28% of Python3 online submissions for Combination Sum.
    Memory Usage: 13.7 MB, less than 6.06% of Python3 online submissions for Combination Sum.
"""


class Solution:
    """
    Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of times.

    Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    """

    def combinationSum(self, candidates, target):
        if not candidates or target <= 0:
            return []
        elif candidates[0] == target:
            follow = self.combinationSum(candidates[1:], target)
            follow.append([candidates[0]])
            return follow

        exist = self.combinationSum(candidates, target - candidates[0])
        not_exist = self.combinationSum(candidates[1:], target)

        for i in exist:
            temp = [candidates[0]]
            temp.extend(i)
            not_exist.append(temp)
        print(f'exist: {exist}, not_exist: {not_exist}, candidates: {candidates}, target: {target}')

        return not_exist


s = Solution()
a = [2, 1, 4]
b = 4
print(s.combinationSum(a, b))


"""
排好序再做搜索，可以跳过许多搜索步骤
回溯法，DFS，backtrack
"""

"""
https://leetcode.com/problems/combination-sum/discuss/16496/Accepted-16ms-c++-solution-use-backtracking-easy-understand.

class Solution {
public:
    std::vector<std::vector<int> > combinationSum(std::vector<int> &candidates, int target) {
        std::sort(candidates.begin(), candidates.end());
        std::vector<std::vector<int> > res;
        std::vector<int> combination;
        combinationSum(candidates, target, res, combination, 0);
        return res;
    }
private:
    void combinationSum(std::vector<int> &candidates, int target, std::vector<std::vector<int> > &res, std::vector<int> &combination, int begin) {
        if (!target) {
            res.push_back(combination);
            return;
        }
        for (int i = begin; i != candidates.size() && target >= candidates[i]; ++i) {
            combination.push_back(candidates[i]);
            combinationSum(candidates, target - candidates[i], res, combination, i);
            combination.pop_back();
        }
    }
};
"""

"""
https://leetcode.com/problems/combination-sum/discuss/16554/Share-My-Python-Solution-beating-98.17/16439

class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(remain, combo, index):
            if remain == 0:
                result.append(combo)
                return
            for i in range(index, len(candy)):
                if candy[i] > remain:
                    # exceeded the sum with candidate[i]
                    break #the for loop
                
                dfs(remain - candy[i], combo + [candy[i]], i)
                
        candy = sorted(candidates)
        result = []
        dfs(target, [], 0)
        return result
"""