class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c = 0
        x = high-low
        if high%2 == 0 and low%2 == 0:
            return int((x)/2)
        else:
            return int(((x)//2) + 1)
   

        