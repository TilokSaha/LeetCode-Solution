class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        Sum = 0
        for i in range(n-1):          # <--------- Another application of Kadane's algorithm
            Sum += prices[i+1] - prices[i]  # <------ Finding the consecutive difference
            if Sum < 0:         # <-------- If the sum of those consecutive difference is negative
                Sum = 0           # <--------- Then we reset the value to 0
            ans = max(ans, Sum)      # <--------- also we are checking whether the new sum is greater or not
        return ans    # <-------- Finding the greatest sum