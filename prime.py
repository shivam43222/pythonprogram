"""
Program to check if a number is prime or not
"""
#  To take input from the user
num = int(input("Enter Number :"))

# check for factors
for num in range(num + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

"""
usage : To run this file please type command on terminal python3 prime.py 
"""


