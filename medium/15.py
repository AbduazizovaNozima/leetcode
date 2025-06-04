# nums = [-1, 0, 1, 2, -1, -4]
# result = []
#
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         for k in range(j+1, len(nums)):
#             triplet = sorted([nums[i], nums[j], nums[k]])
#             if sum(triplet) == 0 and triplet not in result:
#                 result.append(triplet)
#
# print(result)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
