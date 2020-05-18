class Solution:
    def maxProfit(self, prices):
        prev_price = prices[0]
        profits = []
        for price in prices:
            profits.append(price - prev_price)
            prev_price = price
        final_profit = 0
        for p in profits:
            if p > 0:
                final_profit += p
        return final_profit

# A = [7,1,5,3,6,4]
A = [1,2,3,4,5]
sol = Solution()
print(sol.maxProfit(A))
