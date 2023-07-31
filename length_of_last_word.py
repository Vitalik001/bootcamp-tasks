class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        word_length = len(s)
        i=-1
        while s[i]==" ":
            i-=1
        while i>=-word_length and s[i]!=" ":
            i-=1
            length+=1
        return length
