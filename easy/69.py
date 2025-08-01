class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                print(mid)
                break
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        else:
            print(right)


