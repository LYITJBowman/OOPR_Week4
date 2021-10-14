#
# File        : FunctionsDemo2.py  
# Created     : 14/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

def print_lnum(lnum):
    '''
    Prints a welcome message.
    Demonstrates passing a variable into a function

    Parameters:
        lnum    LYIT Student Number

    Returns:
        None
    '''

    print(f'Hi, {lnum}!')
    return


def print_name(student_name):
    '''
    Prints a welcome message.

    Parameters:
        student_name    The students name

    Returns:
        None
    '''

    fname, lname = str(student_name).split(" ")
    print(f'Hi {fname}, welcome to LYIT!')
    return

if __name__ == '__main__':
    print_name('James Bowman')
