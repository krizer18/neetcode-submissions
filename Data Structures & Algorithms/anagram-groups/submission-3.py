class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in strs:
            sortword = tuple(sorted(i))
            result[sortword].append(i)
        
        return list(result.values())