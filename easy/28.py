class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for ind, i in enumerate(haystack):
            if haystack[ind:ind + len(needle)] == needle:
                return ind
        return -1