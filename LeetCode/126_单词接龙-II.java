import java.util.*;

/*
    126. 单词接龙 II
    https://leetcode-cn.com/problems/word-ladder-ii/

    给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。
    转换需遵循如下规则：
    每次转换只能改变一个字母。
    转换后得到的单词必须是字典中的单词。

    执行用时:1190 ms, 在所有 Java 提交中击败了7.05%的用户
    内存消耗:42.8 MB, 在所所有 Java 提交中击败了79.27%的用户
 */


class Solution {
    int pathLength;
    List<List<String>> path = new ArrayList<>();
    HashMap<String, List<String>> transform = new HashMap<>();
    Set<String> visit = new HashSet<>();
    HashMap<String, Integer> layer = new HashMap<>();

    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) return new ArrayList<>();

        if (!wordList.contains(beginWord)) {
            List<String> temp = new ArrayList<>();
            for (String value : wordList) {
                if (arrive(value, beginWord)) {
                    temp.add(value);
                }
            }
            transform.put(beginWord, temp);
        }

        for (int i = 0; i < wordList.size(); ++i) {
            List<String> target = new ArrayList<>();
            for (int j = 0; j < wordList.size(); ++j) {
                if (i == j) continue;
                if (arrive(wordList.get(i), wordList.get(j))) {
                    target.add(wordList.get(j));
                }
            }
            transform.put(wordList.get(i), target);
        }

        layer.put(beginWord, 1);
        Queue<String> candidate = new LinkedList<>();
        candidate.offer(beginWord);
        visit.add(beginWord);
        bfs(candidate);

        visit.clear();
        visit.add(beginWord);
        pathLength = wordList.size() + 2;
        List<String> start = new ArrayList<>();
        start.add(beginWord);
        dfs(beginWord, endWord, start, 1);

        return path;
    }

    public void bfs(Queue<String> candidate) {
        int depth = 1;
        while (!candidate.isEmpty()) {
            depth++;
            int height = candidate.size();
            for (int i = 0; i < height; i++) {
                String start = candidate.poll();
                for (String next : transform.get(start)) {
                    if (!visit.contains(next)) {
                        visit.add(next);
                        layer.put(next, depth);
                        candidate.offer(next);
                    }
                }
            }
        }
    }

    public void dfs(String current, String endWord, List<String> curPath, int length) {
        if (layer.get(current) < length) return;
        if (length >= pathLength && !current.equals(endWord)) return;

        if (current.equals(endWord)) {
            if (length < pathLength) {
                pathLength = length;
                path.clear();
            }
            path.add(new ArrayList<>(curPath));
        } else {
            for (String next : transform.get(current)) {
                if (!visit.contains(next)) {
                    visit.add(next);
                    curPath.add(next);
                    dfs(next, endWord, curPath, length + 1);
                    visit.remove(next);
                    curPath.remove(length);
                }
            }
        }
    }

    public boolean arrive(String a, String b) {
        int difference = 0;
        for (int i = 0; i < a.length(); ++i) {
            if (a.charAt(i) != b.charAt(i)) ++difference;
            if (difference >= 2) return false;
        }
        return true;
    }

}


class LeetCode {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<String> dict = new ArrayList<>(Arrays.asList("hot","cog","dog","tot","hog","hop","pot","dot"));
//        List<String> dict = new ArrayList<>(Arrays.asList("hot","dog","tot","dot"));
        System.out.println(s.findLadders("hot", "dog", dict));
    }
}
