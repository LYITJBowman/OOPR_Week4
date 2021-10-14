#
# File        : FunctionsDemo4.py  
# Created     : 14/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

def change_list(sample_list):
    sample_list = [99,98,97,96]
    print("The sample list included withing the change_list() function is {}".format(sample_list))


def main():
    sample_list = [1,2,3,4,5]
    print("Sample list before: {}".format(sample_list))
    change_list(sample_list)
    print("Sample list after: {}".format(sample_list))

main()