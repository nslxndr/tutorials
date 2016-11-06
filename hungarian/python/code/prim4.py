"""
    Sieve of Erasthotenes prim algorithm
    version 2.0
"""

import math
import time
import sys

max_num = 1001
if len(sys.argv) > 1:        # check command line parameter
    max_num = int(sys.argv[1]) + 1
start_time = time.time()
numbers = range(max_num)     # list of natural numbers to check
for j in range(2, int(math.sqrt(max_num))):
    numbers[j+j::j] = [0 for k in numbers[j+j::j]] # use sieve

prims = sorted(list(set(numbers) - set([0, 1]))) # remove zeros from list
print('ready')
print('%d prims in %f seconds' % (len(prims), time.time() - start_time))
