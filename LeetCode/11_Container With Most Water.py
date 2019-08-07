import time


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        before = time.time()
        result = func(*args, **kwargs)
        after = time.time()
        print(f"elapsed: {after - before}")
        return result

    return wrapper


@decorator
def maxArea(height) -> int:
    # dp = [[0 for _ in range(len(height))] for _ in range(len(height))]
    # for i in range(1, len(height)):
    #     dp[i][i - 1] = min(height[i], height[i - 1])
    #
    # for i in range(2, len(height)):
    #     for j in range(i, len(height)):
    #         dp[j][j - i] = max(min(height[j], height[j - i]) * i,
    #                            dp[j - 1][j - i],
    #                            dp[j][j - i + 1]
    #                            )
    # res = dp[-1][0]

    # mix = 0
    # for i in range(len(height) - 1):
    #     temp = (len(height) - 1 - i) * min(height[-1], height[i])
    #     mix = max(mix, temp)
    # res = max(maxArea(height[:-1]), mix)

    i, j = 0, len(height) - 1
    res = 0
    while i < j:
        print(i, j)
        h = min(height[i], height[j])
        res = max(res, h * (j - i))

        while (height[i] <= h) and (i < len(height) - 1):
            i += 1
        while (height[j] <= h) and (j > 0):
            j -= 1

    return res


a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(a))

'''
https://leetcode.com/problems/container-with-most-water/discuss/6090/Simple-and-fast-C++C-with-explanation
Start by evaluating the widest container, using the first and the last line. 
All other possible containers are less wide, so to hold more water, they need to be higher. 
Thus, after evaluating that widest container, skip lines at both ends that don't support a higher height. 
Then evaluate that new container we arrived at. Repeat until there are no more possible containers left.

int maxArea(vector<int>& height) {
    int water = 0;
    int i = 0, j = height.size() - 1;
    while (i < j) {
        int h = min(height[i], height[j]);
        water = max(water, (j - i) * h);
        while (height[i] <= h && i < j) i++;
        while (height[j] <= h && i < j) j--;
    }
    return water;
}
'''

'''
https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
def maxArea(self, height):
    i, j = 0, len(height) - 1
    water = 0
    while i < j:
        water = max(water, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return water
'''
