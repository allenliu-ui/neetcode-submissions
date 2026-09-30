class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for char in strs[0]:
            candidate_prefix = strs[0][0:i + 1]
            if all(candidate_prefix == w[0:i + 1] for w in strs):
                i += 1
            else:
                return strs[0][0:i]
        return strs[0]
        

                
                
