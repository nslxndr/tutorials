"""
    naive algorith to find prime numbers
    version 1.2
"""

import math
import time
import sys

max_num = 101
if len(sys.argv) > 1:        # check command line parameter
    max_num = int(sys.argv[1]) + 1
start_time = time.time()
prims = []                   # list of prims
for p in range(2, max_num):  # find prims up to max_num
    for divider in range(2, int(math.sqrt(p))+1):
        if p % divider == 0: # remainder of division is zero
            break            # divider found no need to continue
    else:
        prims.append(p)      # store prime number
print('ready')
print('%d prims in %f seconds' % (len(prims), time.time() - start_time))
