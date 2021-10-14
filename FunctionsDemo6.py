#
# File        : FunctionsDemo6.py  
# Created     : 14/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
def overloading_sample(num_1, num_2=10):
    total_inner = num_1 + num_2
    print("Inside function total is: {}".format(total_inner))
    return total_inner


if __name__ == '__main__':
    total = overloading_sample(99, 1000)
    print("In main, total is: {}".format(total))
    total = overloading_sample(50)
    print("In main, total is: {}".format(total))