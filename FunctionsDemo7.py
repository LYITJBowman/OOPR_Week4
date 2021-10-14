#
# File        : FunctionsDemo7.py  
# Created     : 14/10/2021
# Author      : James Bowman
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

def multi_sample(num_1, num_2=10):
    num_1 = num_1 * 2
    num_2 = 123
    return num_1, num_2


def list_rtn_sample2(list1):
    list1 = list1 * 2
    return list1


def list_rtn_sample():
    ages = [19, 21, 20]
    return ages


if __name__ == '__main__':
    val_1, val_2 = multi_sample(4, 6)
    print(f"Value 1 is {val_1} and value 2 is {val_2}")
    print("\nFull return was: {}".format(multi_sample(12, 14)))
    print("\nList example: {}".format(list_rtn_sample()))
    print("\n")
    print(list_rtn_sample2([1,2,3]))
