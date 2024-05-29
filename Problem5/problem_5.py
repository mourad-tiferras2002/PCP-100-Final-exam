#!/usr/bin/env python3

import sys

""" Problem5: just promting the user for a number and make the division"""

try:
    num = float(input("Please enter a number: "))
    resulta = float(100/num)
except ZeroDivisionError:
    print("\n Division by zero is not allowed.")
    sys.exit(1)
except:
    print("Error: u should ennter a no-null number")
    sys.exit(1)

print(f"\n The result of division is {resulta}")
