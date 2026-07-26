class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        transaction = 0

        for price in prices:

            min_price = min(min_price, price)
            
            transaction = max(price - min_price, transaction)
        
        return transaction