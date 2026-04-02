class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited = set()

        for i in range(len(strs)):
            if i in visited:
                continue

            group = [strs[i]]
            visited.add(i)

            for j in range(i + 1, len(strs)):
                if j not in visited and self.isAnagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited.add(j)

            result.append(group)

        return result


