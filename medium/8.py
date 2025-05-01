class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        if s[0] in ['+', '-']:
            start = 1
        else:
            start = 0

        count = 0
        for i in range(start,len(s)):
            if s[i].isdigit():
                count += 1
            else:
                break
        if count == 0:
            return 0 
        else:
            result = int(s[0:start + count])

            if result < -2147483648:
                return -2147483648
            elif result > 2147483647:
                return 2147483647
            else:
                return result