import math 
import os
import random
import re
import sys

from sqlalchemy import between

def check(num):
    if num%2!=0:
        print(f"[{num}] is Weird")
    elif num in range(2,6):
        print(f"[{num}] is Not Weird")
    elif num is range(6,21):
        print(f"[{num}] is Weird")
    else:
        print(f"[{num}] is Not Weird")


if __name__ == "__main__":
    n = int(input().strip())
    check(n)