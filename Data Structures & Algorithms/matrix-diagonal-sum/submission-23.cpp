class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int s = 0;

        if (mat.size() % 2 == 0) {
            int c = 0;

            for (int i = 0; i < mat.size(); i++) {
                s = s + mat[i][c];
                c++;
            }

            c = 0;
            for (int j = -1; j >= -mat.size(); j--) {
                s = s + mat[mat.size() + j][c];
                c++;
            }
        } 
        else {
            int c = 0;

            for (int i = 0; i < mat.size(); i++) {
                s = s + mat[i][c];
                c++;
            }

            c = 0;
            for (int j = -1; j >= -mat.size(); j--) {
                if (j == -(mat.size() / 2 + 1)) {
                    c++;
                    continue;
                }

                s = s + mat[mat.size() + j][c];
                c++;
            }
        }

        return s;
    }
};