# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import math

three_max = int(math.floor(999 / 3))

three_sum = 0

for i in range(0, three_max + 1):
    three_sum += i * 3

five_max = int(math.floor(999 / 5))

five_sum = 0

for i in range(0, five_max + 1):
    five_sum += i * 5

# multiples of both 3 and 5
fifteen_max = int(math.floor(999 / 15))

fifteen_sum = 0

for i in range(0, fifteen_max + 1):
    fifteen_sum += i * 15
    


## Now we have to take out the duplicates------
solution = three_sum + five_sum - fifteen_sum

print(solution)
# 233168
