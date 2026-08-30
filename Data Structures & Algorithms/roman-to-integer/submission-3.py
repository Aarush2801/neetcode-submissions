class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        su = 0

        for num in range(len(s)):
            if num + 1 < len(s) and values[s[num]] < values[s[num + 1]]:
                su -= values[s[num]]
            else:
                su += values[s[num]]

        return su




            

        