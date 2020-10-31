import java.util.*;

/*
    381. O(1) 时间插入、删除和获取随机元素 - 允许重复
    https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

    设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。
    注意: 允许出现重复元素。
    insert(val)：向集合中插入元素 val。
    remove(val)：当 val 存在时，从集合中移除一个 val。
    getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。

    执行用时：15 ms, 在所有 Java 提交中击败了79.86%的用户
    内存消耗：45.6 MB, 在所有 Java 提交中击败了38.55%的用户
 */


class RandomizedCollection {
    Map<Integer, Set<Integer>> index;
    List<Integer> numbers;

    /** Initialize your data structure here. */
    public RandomizedCollection() {
        numbers = new ArrayList<>();
        index = new HashMap<>();
    }

    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
        numbers.add(val);
        Set<Integer> set = index.getOrDefault(val, new HashSet<Integer>());
        set.add(numbers.size() - 1);
        index.put(val, set);
        return set.size() == 1;
    }

    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
        if (index.containsKey(val)) {
            int firstIndex = index.get(val).iterator().next();
            int lastNumber = numbers.get(numbers.size() - 1);
            if (lastNumber == val) {
                index.get(lastNumber).remove(numbers.size() - 1);
            } else {
                index.get(val).remove(firstIndex);
                numbers.set(firstIndex, lastNumber);
                index.get(lastNumber).remove(numbers.size() - 1);
                index.get(lastNumber).add(firstIndex);
            }
            
            if (index.get(val).size() == 0) {
                index.remove(val);
            }
            numbers.remove(numbers.size() - 1);
            return true;
        }
        return false;
    }

    /** Get a random element from the collection. */
    public int getRandom() {
        return numbers.get((int)(Math.random() * numbers.size()));
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */



class RandomizedCollection2 {
    Map<Integer, Set<Integer>> idx;
    List<Integer> nums;

    /** Initialize your data structure here. */
    public RandomizedCollection() {
        idx = new HashMap<Integer, Set<Integer>>();
        nums = new ArrayList<Integer>();
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
        nums.add(val);
        Set<Integer> set = idx.getOrDefault(val, new HashSet<Integer>());
        set.add(nums.size() - 1);
        idx.put(val, set);
        return set.size() == 1;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
        if (!idx.containsKey(val)) {
            return false;
        }
        Iterator<Integer> it = idx.get(val).iterator();  
        int i = it.next();
        int lastNum = nums.get(nums.size() - 1);
        nums.set(i, lastNum);
        idx.get(val).remove(i);
        idx.get(lastNum).remove(nums.size() - 1);
        if (i < nums.size() - 1) {
            idx.get(lastNum).add(i);
        }
        if (idx.get(val).size() == 0) {
            idx.remove(val);
        }
        nums.remove(nums.size() - 1);
        return true;
    }
    
    /** Get a random element from the collection. */
    public int getRandom() {
        return nums.get((int) (Math.random() * nums.size()));
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/solution/o1-shi-jian-cha-ru-shan-chu-he-huo-qu-sui-ji-yua-5/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。