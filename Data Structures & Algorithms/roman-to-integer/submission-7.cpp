class Solution {
public:
    int romanToInt(string s) {
        int su = 0;

        for (int num = 0; num < s.length(); num++) {
            int current;

            if (s[num] == 'I') current = 1;
            else if (s[num] == 'V') current = 5;
            else if (s[num] == 'X') current = 10;
            else if (s[num] == 'L') current = 50;
            else if (s[num] == 'C') current = 100;
            else if (s[num] == 'D') current = 500;
            else current = 1000;

            if (num + 1 < s.length()) {
                int next;

                if (s[num + 1] == 'I') next = 1;
                else if (s[num + 1] == 'V') next = 5;
                else if (s[num + 1] == 'X') next = 10;
                else if (s[num + 1] == 'L') next = 50;
                else if (s[num + 1] == 'C') next = 100;
                else if (s[num + 1] == 'D') next = 500;
                else next = 1000;

                if (current < next)
                    su -= current;
                else
                    su += current;
            }
            else {
                su += current;
            }
        }

        return su;
    }
};