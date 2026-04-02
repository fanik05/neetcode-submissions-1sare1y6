class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstString = sorted(s)
        secondString = sorted(t)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if firstString[i] != secondString[i]:
                return False
        
        return True
            