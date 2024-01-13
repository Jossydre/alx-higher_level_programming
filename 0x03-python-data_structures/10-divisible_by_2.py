#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    for d in my_list:
        if (d % 2 == 0):
            newlist.append(True)
        else:
            newlist.append(False)
    return (newlist)
