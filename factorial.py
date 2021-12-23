"""
program to find the factorial of a number provided by the user.
"""
# To take input from the user
num = int(input("enter a number: "))
#initialize
fac = 1
for i in range(1, num + 1):
    fac = fac * i
 
print("factorial of ", num, " is ", fac)

"""
usage : To run this file please type command on terminal python3 factorial.py 
"""