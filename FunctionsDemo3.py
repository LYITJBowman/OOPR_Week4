#
# File        : FunctionsDemo3.py  
# Created     : 14/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

num = 3
inc_by = 2

def increase_value(original_value, increment_by):
    print("Inside Method")
    print("original_value {0} id {1}".format(original_value, id(original_value)))
    print("increment_by {0} id {1}".format(increment_by, id(increment_by)))
    original_value += increment_by
    print("Updated original_value {0} (new)id {1}\n".format(original_value, id(original_value)))


if __name__ == '__main__':
    print("Called in main")
    print("num {0} numid {1}".format(num, id(num)))
    print("inc_by {0} inb_by id {1}\n".format(inc_by, id(inc_by)))

    increase_value(num, inc_by)
    print("Called in main after calling function")
    print("num {0} numid {1}".format(num, id(num)))
    print("inc_by {0} inb_by id {1}\n".format(inc_by, id(inc_by)))