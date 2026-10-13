class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for words in strs:
            count = [0] * 26

            for c in words:
                count[ord(c) - ord("a")] += 1

            hashmap[tuple(count)].append(words)
        return list(hashmap.values())
        
        