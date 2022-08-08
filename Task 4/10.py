#!python3

import operator
import string

def print_rangoli(n):
    mid = n-1
    for row in range(n*2-1):
        line = ""
        for col in range(n*2-1):
            d = abs(row-mid) + abs(col-mid)
            if (col>0): line += "-"
            if d>=n: line += "-"
            else: line += string.ascii_lowercase[d]
        print(line)
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)