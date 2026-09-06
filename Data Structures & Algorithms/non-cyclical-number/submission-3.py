class Solution:
    def isHappy(self, n: int) -> bool:
        l = []
        flag = True
        num = n
        while flag == True:
            s = 0
            for d in str(num):
                s = s + int(d)**2

            if s == 1:
                flag = False
            else:
                l.append(n)
                num = s

        