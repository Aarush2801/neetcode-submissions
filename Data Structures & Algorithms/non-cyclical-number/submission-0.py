class Solution:
    def isHappy(self, n: int) -> bool:
        l = []
        while Flag == True:
            s = 0
            for d in num(n):
                s = s + int(d)**2

            if s == 1:
                Flag = False
            else:
                l.append(n)
                num = s

        