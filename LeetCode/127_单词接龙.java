import java.util.*;

/*
    127. 单词接龙
    https://leetcode-cn.com/problems/word-ladder/

    给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。

    执行用时：1327 ms, 在所有 Java 提交中击败了12.81%的用户
    内存消耗：41 MB, 在所有 Java 提交中击败了33.33%的用户
 */


class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}


class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) return 0;
        HashMap<String, List<String>> transform = new HashMap<>();

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

        Queue<String> candidate = new LinkedList<>();
        candidate.offer(beginWord);
        Set<String> visit = new HashSet<>();
        visit.add(beginWord);
        int depth = 0;

        while (!candidate.isEmpty()) {
            ++depth;
            int layer = candidate.size();
            for (int i = 0; i < layer; ++i) {
                String s = candidate.poll();
                for (String neigh : transform.get(s)) {
                    if (neigh.equals(endWord)) return depth + 1;
                    if (!visit.contains(neigh)) {
                        candidate.offer(neigh);
                        visit.add(neigh);
                    }
                }
            }
        }
        return 0;
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


class Solution_2 {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) {
            return 0;
        }
        // visited修改为boolean数组
        boolean[] visited = new boolean[wordList.size()];
        int idx = wordList.indexOf(beginWord);
        if (idx != -1) {
            visited[idx] = true;
        }
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        int count = 0;
        while (queue.size() > 0) {
            int size = queue.size();
            ++count;
            while (size-- > 0) {
                String start = queue.poll();
                for (int i = 0; i < wordList.size(); ++i) {
                    // 通过index判断是否已经访问
                    if (visited[i]) {
                        continue;
                    }
                    String s = wordList.get(i);
                    if (!canConvert(start, s)) {
                        continue;
                    }
                    if (s.equals(endWord)) {
                        return count + 1;
                    }
                    visited[i] = true;
                    queue.offer(s);
                }
            }
        }
        return 0;
    }

    public boolean canConvert(String s1, String s2) {
        // 因为题目说了单词长度相同，可以不考虑长度问题
        // if (s1.length() != s2.length()) return false;
        int count = 0;
        for (int i = 0; i < s1.length(); ++i) {
            if (s1.charAt(i) != s2.charAt(i)) {
                ++count;
                if (count > 1) {
                    return false;
                }
            }
        }
        return count == 1;
    }
}

// 作者：jzj1993
// 链接：https://leetcode-cn.com/problems/word-ladder/solution/suan-fa-shi-xian-he-you-hua-javashuang-xiang-bfs23/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution_3 {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        int end = wordList.indexOf(endWord);
        if (end == -1) {
            return 0;
        }
        wordList.add(beginWord);
        
        // 从两端BFS遍历要用的队列
        Queue<String> queue1 = new LinkedList<>();
        Queue<String> queue2 = new LinkedList<>();
        // 两端已经遍历过的节点
        Set<String> visited1 = new HashSet<>();
        Set<String> visited2 = new HashSet<>();
        queue1.offer(beginWord);
        queue2.offer(endWord);
        visited1.add(beginWord);
        visited2.add(endWord);
        
        int count = 0;
        Set<String> allWordSet = new HashSet<>(wordList);

        while (!queue1.isEmpty() && !queue2.isEmpty()) {
            count++;
            if (queue1.size() > queue2.size()) {
                Queue<String> tmp = queue1;
                queue1 = queue2;
                queue2 = tmp;
                Set<String> t = visited1;
                visited1 = visited2;
                visited2 = t;
            }
            int size1 = queue1.size();
            while (size1-- > 0) {
                String s = queue1.poll();
                char[] chars = s.toCharArray();
                for (int j = 0; j < s.length(); ++j) {
                    // 保存第j位的原始字符
                    char c0 = chars[j];
                    for (char c = 'a'; c <= 'z'; ++c) {
                        chars[j] = c;
                        String newString = new String(chars);
                        // 已经访问过了，跳过
                        if (visited1.contains(newString)) {
                            continue;
                        }
                        // 两端遍历相遇，结束遍历，返回count
                        if (visited2.contains(newString)) {
                            return count + 1;
                        }
                        // 如果单词在列表中存在，将其添加到队列，并标记为已访问
                        if (allWordSet.contains(newString)) {
                            queue1.offer(newString);
                            visited1.add(newString);
                        }
                    }
                    // 恢复第j位的原始字符
                    chars[j] = c0;
                }
            }
        }
        return 0;
    }
}

// 作者：jzj1993
// 链接：https://leetcode-cn.com/problems/word-ladder/solution/suan-fa-shi-xian-he-you-hua-javashuang-xiang-bfs23/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。