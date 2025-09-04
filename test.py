nums = [3, 3]
target = 6


# for i in range(0, len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i, j)



seen = {}  # qiymat: index
for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
        print([seen[diff], i])
    seen[num] = i
