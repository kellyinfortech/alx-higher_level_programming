#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    sum_total = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            sum_total += 1
        except:
            continue
    print()
    return sum_total
