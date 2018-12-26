# File: chaos.py
# A simple program illustrating chaotic behavior.
"""
    Benjamin Chen
    CSC161 Lab1 TR 1230-145
"""

def main():
    print("This program illustrates a chaotic function")
    n = eval(input("How many numbers should I print? "))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

main()