class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        result = 0
        for index, value in enumerate(s):
            result += roman_dict[value]

            if index < len(s) - 1 and roman_dict[value] < roman_dict[s[index + 1]]:
                result -= 2 * roman_dict[value]

        return result