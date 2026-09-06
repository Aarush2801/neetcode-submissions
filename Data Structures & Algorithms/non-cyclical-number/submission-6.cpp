class Solution {
public:
    bool isHappy(int n) {
        vector<int> l;
        bool flag = true;
        int num = n;

        while (flag) {
            int s = 0;

            for (char d : to_string(num)) {
                s += (d - '0') * (d - '0');
            }

            if (s == 1) {
                flag = false;
            }
            else if (find(l.begin(), l.end(), num) != l.end()) {
                return false;
            }
            else {
                l.push_back(num);
                num = s;
            }
        }

        return true;
    }
};