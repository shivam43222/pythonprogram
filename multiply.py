"""
Multiplication table (from 1 to 10) in Python
"""
# take input from the user
num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

"""
usage : To run this file please type command on terminal python3 multiply.py 
"""