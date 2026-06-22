class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            sortword = tuple(sorted(s))
            seen[sortword].append(s)
        return list(seen.values())

