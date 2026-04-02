class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_first_string = sorted(s)
        sorted_second_string = sorted(t)

        for i in range(len(s)):
            if sorted_first_string[i] != sorted_second_string[i]:
                return False

        return True



        