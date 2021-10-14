#
# File        : QuestionOne.py  
# Created     : 14/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
import platform
import os


if __name__ == '__main__':
    print("Machine\t\t\t{}".format(platform.machine()))
    print("Node\t\t\t{}".format(platform.node()))
    print("Platform\t\t{}".format(platform.platform()))
    envdict = dict(os.environ)
    print("Path\t\t\t{}".format(envdict["PATH"]))

