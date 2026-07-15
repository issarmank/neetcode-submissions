class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sortedS = ''.join(sorted(word))
            anagram_map[sortedS].append(word)
        return list(anagram_map.values())