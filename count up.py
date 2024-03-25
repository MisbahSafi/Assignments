#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ZiaUllah
#
# Created:     19/02/2024
# Copyright:   (c) ZiaUllah 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def countup(n):
    if n>=0:
        print("Welcome!")
    else:
        print(n)
        countup(n+1)

countup(-3)
