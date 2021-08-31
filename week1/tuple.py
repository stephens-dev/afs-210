from collections import defaultdict
classes = (
    ('VII', 1),
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
)

nums = defaultdict(list)

for numural, number in classes:
    nums[numural].append(number)

print(nums)