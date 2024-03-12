class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        maxcount=0
        while right<len(prices):
            diff=prices[right]-prices[left]
            if prices[right]>prices[left]:
                maxcount=max(maxcount,diff)
            else:
                left=right 
            right+=1
        return maxcount