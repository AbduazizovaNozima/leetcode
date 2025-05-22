class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        min_str = min(strs, key=len)
        result = []

        for i in range(len(min_str)):
            ch = min_str[i]
            for s in strs:
                if s[i] != ch:
                    return "".join(result)  
            result.append(ch)
        return "".join(result)