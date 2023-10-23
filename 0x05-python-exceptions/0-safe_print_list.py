#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    sum_total = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            sum_total += 1
        except (ValueError, TypeError):
            continue
    print("")
    return(sum_total)
