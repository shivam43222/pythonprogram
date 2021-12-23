"""
program to check if the input number is odd or even.
"""

# take input from the user
num = int(input("Number: "))
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number
mod = num % 2
if mod == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

"""
usage : To run this file please type command on terminal python3 even.py 
"""