class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_dict = dict()
        for char in t:
            if t_dict.get(char) is not None:
                t_dict[char]+=1
            else:
                t_dict[char] = 1
        for char in s:
            t_dict[char]-=1
        for key, value in t_dict.items():
            if value == 1:
                return key