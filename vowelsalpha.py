"""
program to check if a given character is vowel or consonant.
"""
#taking user input
ch = input("Enter a character: ")
# condition to check whether a character is vowel or not.
if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

"""
usage : To run this file please type command on terminal python3 vowelsalpha.py 
"""