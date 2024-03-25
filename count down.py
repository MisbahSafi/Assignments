#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ZiaUllah
#
# Created:     19/02/2024
# Copyright:   (c) ZiaUllah 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def countdown(n):
    if n <=0:
        print("Blast Off!")
    else:
        print(n)
        countdown(n-1)

countdown (10)
