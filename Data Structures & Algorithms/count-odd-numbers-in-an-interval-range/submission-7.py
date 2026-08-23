class Solution:
    def countOdds(self, low: int, high: int) -> int:

        return (high + 1) // 2 - low // 2
        '''c = 0
        
        if high%2 == 0 and low%2 == 0:
            return int((high-low)/2)
        else:
            return int(((high-low)//2) + 1)'''
   

        