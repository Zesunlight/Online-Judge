class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0

        buy = prices[0]
        sell = max(prices[1:])
        profit = max(sell - buy, 0)

        for i in range(1, len(prices) - 1):
            if prices[i] < buy:
                buy = prices[i]
            sell = prices[i + 1]
            if sell - buy > profit:
                profit = sell - buy

        return profit


s = Solution()
a = [7, 1, 5, 3, 6, 4]
# a = [7, 6, 4, 3, 1]
print(s.maxProfit(a))


"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-:)-(In-case-if-interviewer-twists-the-input)
Kadane's Algorithm
Here, the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) of the original array, and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.

public int maxProfit(int[] prices) {
    int maxCur = 0, maxSoFar = 0;
    for(int i = 1; i < prices.length; i++) {
        maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
        maxSoFar = Math.max(maxCur, maxSoFar);
    }
    return maxSoFar;
}


https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39039/Sharing-my-simple-and-clear-C++-solution
int maxProfit(vector<int> &prices) {
    int maxPro = 0;
    int minPrice = INT_MAX;
    for(int i = 0; i < prices.size(); i++){
        minPrice = min(minPrice, prices[i]);
        maxPro = max(maxPro, prices[i] - minPrice);
    }
    return maxPro;
}

public int maxProfit(int[] prices) {
    if(prices == null || prices.length < 2) return 0;      
    int maxProfit = 0, minPrice = prices[0];
    
    for(int i = 1; i < prices.length; i++) {
        if(prices[i] > prices[i - 1]) {
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);       
        } else {
             minPrice = Math.min(minPrice, prices[i]);
        }
    }

    return maxProfit;
}
"""