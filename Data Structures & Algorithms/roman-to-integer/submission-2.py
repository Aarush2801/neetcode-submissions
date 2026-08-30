class Solution:
    def romanToInt(self, s: str) -> int:
        su = 0

        for num in range(len(s)):
            if num + 1 < len(s) and s[num] == 'I' and s[num + 1] != 'I':
                su -= 1
            elif s[num] == 'I':
                su += 1

        return su




            

        