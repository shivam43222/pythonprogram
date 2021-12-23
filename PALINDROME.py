"""
checking a number is palindrome 
""" 

#taking user input
n=int(input("Enter number:"))
#temporary variable
temp=n
rev=0
# used while loop
while(n>0):
    l_dig=n%10
    rev=rev*10+l_dig
    n=n//10
# condition check 
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!") 

"""
usage : To run this file please type command on terminal python3 palindrome.py 
"""