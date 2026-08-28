class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)%2 == 0:
            s = 0
            c = 0
            for i in range(len(mat)):
                s = s + mat[i][c]
                c += 1
            
            c = -1
            for j in range(-1,-len(mat)-1,-1):
                s = s+ mat[i][c]
                c = c -1
        else:
            s = 0
            c = 0
            for i in range(len(mat)):
                if i == len(mat)//2 + 1:
                    continue
                else:
                    s = s + mat[i][c]
                    c += 1
            
            c = -1
            for j in range(-1, -len(mat) -1,-1):
                s = s+ mat[j][c]
                c = c -1

        return s


        
        

            
            

        