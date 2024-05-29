#!/usr/bin/env python3

"""
Problem4: a fun that return the max
"""

def max_number(x, y, z):
    """max_number - A func that return the maximum number

    Args:
        x (int or float): A number to check if it's tha maximum
        y (int or float): A number to check if it's tha maximum
        z (int or float): A number to check if it's tha maximum
    Returns:
        maxi: The maximum number
    """
    if x >= y and x >= z:
        maxi = x
    if y >= x and y >= z:
        maxi = y
    if z >= x and z >= y:
        maxi = z
    return maxi



def main():
    """The main func that will be executed to demonstrate how to call max_number func
    """
    num1 = -88
    num2 = 1985
    num3 = 188
    # This how the func it call by puting it's prototype and it's arguments
    maximum = max_number(num1, num2, num3)
    print(f" The maximum number is {maximum}")


if __name__ == "__main__":
    main()
