class Solution:
    def isHappy(self, n: int) -> bool:
        l = []
        flag = True
        while flag == True:
            s = 0
            for d in num(n):
                s = s + int(d)**2

            if s == 1:
                flag = False
            else:
                l.append(n)
                num = s

        