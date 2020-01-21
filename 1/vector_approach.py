# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import math
import numpy as np

three_max = int(math.floor(999 / 3))

three_vec = np.empty([three_max + 1])

for i in range(three_max + 1):
    three_vec[i] = i * 3


five_max = int(math.floor(999 / 5))

five_vec = np.empty([five_max + 1])

for i in range(five_max + 1):
    five_vec[i] = i * 5

all = np.append(three_vec, five_vec)

sum(np.unique(all))

# 233168.0
