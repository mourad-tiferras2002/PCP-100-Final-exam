#!/usr/bin/env python3

import sys
"""
Problem2: promt the user for an age and check if they are a teenager (ages 13-19) or not
"""

try:
    age = float(input(" Enter an age:  "))
    age = int(age)
except:
    print("The age must be a number")
    sys.exit(1)
if age >= 13 and age <= 19:
    print("The age is concidered as a teenager")
else:
    print("The age is not a teenager")
