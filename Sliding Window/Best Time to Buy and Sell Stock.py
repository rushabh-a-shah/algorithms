class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[sell] <= prices[buy]:
                buy, sell = sell, sell + 1
            else:
                maxProfit = max(maxProfit, (prices[sell] - prices[buy]))
                sell += 1
        return maxProfit
