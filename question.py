# names = ["1", "2", "3"]
# [1, 2, 3]
def random_groups(names):
  # shuffle
  res = []
  group_size = 3
  if len(names) < group_size:
    return [names]

  n = len(names)
  group = []
  for name in names:
    if len(group) <= group_size:
      group.append(name)
      if len(group) == group_size:
        res.append(group)
        group = []

  remaing = n % group_size
  if remaing > 0:
    res[-1] += names[-remaing:]
  return res

# [1, 2, 3], [4, 5, 6], 7
# 7 % 3 = 1
# 1.. 7
# [[1, 2, 3], [4, 5, 6], [7]]
#  ^0         ^1        

names = ["1", "2", "3"]
groups = [["1", "2", "3"]]
assert random_groups(names) == groups
# 3-5 names, random

names = ["1", "2"]
groups = [["1", "2"]]
assert random_groups(names) == groups

names = ["1", "2", "3", "4", "5", "6", "7"]
groups = [["1", "2", "3"], ["4", "5", "6", "7"]]
assert random_groups(names) == groups

# shuffle names to generate random groups


# ["1", "2", "3", "4", "5", "6", "7"]
# num_groups = 7 // 3 = 2
# [1, 2, 3], [4, 5, 6, 7]

# [1..10]
# num_groups 10 // 3 = 3
# [1..3], [4..6], [7..10]

# [1..10]
# num_groups 10 // 4 = 2
# [1..4], [5..10]x




