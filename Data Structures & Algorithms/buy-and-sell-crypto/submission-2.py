class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        transaction = 0

        for i in range(len(prices)):

            if min_price > prices[i]:
                min_price = prices[i]
            
            current_transaction = prices[i] - min_price

            if transaction < current_transaction:
                transaction = current_transaction
        
        return transaction