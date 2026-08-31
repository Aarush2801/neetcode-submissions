class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s = s+str(i)
        hmm = int(s)
        hmmm = hmm+1
        return list(str(hmmm))
        