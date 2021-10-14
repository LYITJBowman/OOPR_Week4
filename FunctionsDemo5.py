#
# File        : FunctionsDemo5.py  
# Created     : 14/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

def overloading_sample(num_1, num_2=10):
    total = 0
    total = num_1 + num_2
    print("inside function total: {}".format(total))
    return


total = 0
overloading_sample(99,1000)
overloading_sample(50)
print("Outside of function total: {}".format(total))
