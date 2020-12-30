from itertools import permutations
from itertools import repeat
from itertools import combinations

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 25, 74, 54, 20, 14, 36, 95]
new = [el for el in my_list if my_list.count(el) == 1]
print(new)
