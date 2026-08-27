class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        acc = numBottles
        while numBottles >= numExchange:
            acc = acc + numBottles//numExchange 
            numBottles = numBottles//numExchange + numBottles%numExchange
        return acc


    
