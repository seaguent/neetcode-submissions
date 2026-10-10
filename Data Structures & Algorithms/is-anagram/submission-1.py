class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for n in s:
            if n in seen:
                seen[n] +=1
            else:
                seen[n] = 1
        for c in t:
            if c in seen:
                seen[c] -= 1
            else:
                return False

        for v in seen.values():
            if v != 0:
                return False
        return True    

