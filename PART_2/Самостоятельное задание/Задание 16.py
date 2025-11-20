# Дан список nums = [2, 7, 4, 9, 6, 5].
# Используя while, удалить все чётные числа из этого списка

nums = [2, 7, 4, 9, 6, 5]
i = 0

while i < len(nums):
    if nums[i] % 2 == 0:
        nums.remove(nums[i])
    else:
        i += 1

print(nums)


