class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=''
        i=len(word1)
        j=len(word2)
        for m in range(min(i,j)):
            word3+=word1[m]+word2[m]
        return (word3+word1[m+1:]+word2[m+1:])
