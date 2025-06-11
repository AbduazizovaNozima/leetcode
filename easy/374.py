def guess(num: int) -> int:
    class Solution:
        def guessNumber(self, n: int) -> bool:

            low = 1
            high = n
            while low <= high:
                mid = (low + high) // 2
                g = guess(mid)

                if g == 0:
                    return mid
                elif g < 0:
                    high = mid - 1
                else:
                    low = mid + 1
