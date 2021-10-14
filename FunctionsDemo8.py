#
# File        : FunctionsDemo8.py  
# Created     : 14/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
import random
import os
import sys
import math


for i in range(5):
    print(random.randint(1,10))

env_tup = tuple(os.environ)
for i in range(5):
    sys.stdout.write("{} ".format(env_tup[i]))

print("\n\nThe factorial of 4 is (1x2x3x4) {}".format(math.factorial(4)))
print("Mathematics value pi is: {}".format(math.pi))

if __name__ == '__main__':
    pass
