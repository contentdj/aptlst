# names = ["1", "2", "3"]
# [1, 2, 3]
import math
from random import shuffle
# def random_groups(names):
#   # shuffle
#   res = []
#   group_size = 3
#   if len(names) < group_size:
#     return [names]

#   n = len(names)
#   group = []
#   for name in names:
#     if len(group) <= group_size:
#       group.append(name)
#       if len(group) == group_size:
#         res.append(group)
#         group = []

#   remaing = n % group_size
#   if remaing > 0:
#     res[-1] += names[-remaing:]
#   return res


def random_groups2(names, group_size):
  # shuffle
  # shuffle(names)
  res = []
  if len(names) <= group_size:
    return [names]
  
  n = len(names)
  num_groups = math.floor(n / group_size)

  res = []
  count = 0
  # names = ["1", "2", "3",  | "4", "5", "6", | "7"]
  for i in range(num_groups):    
    group = []
    j = 0
    while j < group_size:
      group.append(names[count])
      j+=1
      count += 1
    res.append(group)

  # 7   
  if count < n:
    i = 0
    # while i < num_groups and count < n:     
    #   res[i].append(names[count])
    #   count+=1
    #   i+=1

    # heidi: below fixed the bug with 11. Bug was on i < num_groups. So it only go thru the groups once
    while count < n:     
      res[i].append(names[count])
      count+=1
      i = (i+1) % num_groups
    
  return res


# [1, 2, 3], [4, 5, 6], 7

# [1, 2, 3], [4, 5, 6], 7
# 7 % 3 = 1
# 1.. 7
# [[1, 2, 3], [4, 5, 6], [7]]
#  ^0         ^1        

names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
# names = ["1", "2", "3", "4",  | "5", "6", "7", "8", | "9", "10", "11"]
groups = [['1', '2', '3', '4', '9'], ['5', '6', '7', '8', '10', '11']]
print(random_groups2(names, 4))
# assert random_groups2(names, 4) == groups

names = ["1", "2", "3"]
groups = [["1", "2", "3"]]
assert random_groups2(names, 3) == groups
# 3-5 names, random

names = ["1", "2"]
groups = [["1", "2"]]
assert random_groups2(names, 3) == groups

names = ["1", "2", "3", "4", "5", "6", "7"]
groups = [["1", "2", "3", "7"], ["4", "5", "6"]]
assert random_groups2(names, 3) == groups

names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
groups = [["1", "2", "3", "10"], ["4", "5", "6", "11"], ["7", "8", "9"]]
assert random_groups2(names, 3) == groups

# names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
# # names = ["1", "2", "3", "4",  | "5", "6", "7", "8", | "9", "10", "11"]
# groups = [['1', '2', '3', '4', '9'], ['5', '6', '7', '8', '10']]
# assert random_groups2(names, 5) == groups

# names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
# print(random_groups2(names))
